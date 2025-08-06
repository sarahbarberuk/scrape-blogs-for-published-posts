from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
from datetime import datetime

from scraper_config import SCRAPER_CONFIGS  # import config


def scrape_blog_with_playwright(config):
    print(f"[INFO] Launching browser for: {config['url']}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        wait_until = config.get("wait_until", "networkidle")  # default to "networkidle"
        page.goto(config['url'], wait_until=wait_until, timeout=60000)

        selector = config.get('load_more_selector')
        if selector:
            while True:
                try:
                    button = page.locator(selector)
                    if button.is_visible() and button.is_enabled():
                        print("[INFO] Clicking 'Load more'...")
                        button.click()
                        page.wait_for_timeout(config.get('load_more_delay', 2000))
                    else:
                        break
                except:
                    break

        page.wait_for_timeout(1000)
        html = page.content()
        browser.close()
        return html


def parse_blog_html(html, config, client_name):
    soup = BeautifulSoup(html, 'html.parser')
    posts = []

    for i, post in enumerate(soup.select(config['post_selector']), start=1):
        title_tag = post.select_one(config['title_selector'])
        date_tag = post.select_one(config['date_selector'])

        title = title_tag.get_text(strip=True) if title_tag else 'Untitled'
        date = date_tag.get_text(strip=True) if date_tag else ''
        href = post.get('href', '')
        link = f"{config['base_url']}{href}" if href.startswith('/') else href

        posts.append((title, link, date, client_name))
        print(f"[DEBUG] ({client_name}) Post {i}: Title='{title}', URL='{link}', Date='{date}'")

    print(f"[INFO] ({client_name}) Found {len(posts)} posts")
    return posts


def write_csv(all_posts, filename):
    print(f"[INFO] Writing to CSV: {filename}")
    now = datetime.utcnow().isoformat()
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'URL', 'Published Date', 'Client', 'Scraped At'])
        for post in all_posts:
            writer.writerow([*post, now])
    print(f"[INFO] Saved {len(all_posts)} posts to {filename}")


def main():
    all_posts = []
    output_file = 'published_articles.csv'

    for client_name, config in SCRAPER_CONFIGS.items():
        print(f"\n[INFO] Scraping client: {client_name}")
        html = scrape_blog_with_playwright(config)

        if 'display_name' not in config:
            raise KeyError(f"[ERROR] 'display_name' is missing in config for client: {client_name}")
        posts = parse_blog_html(html, config, config['display_name'])

        all_posts.extend(posts)

    if all_posts:
        write_csv(all_posts, output_file)
    else:
        print("[WARN] No posts scraped from any client.")

    print("[INFO] Script finished")


if __name__ == '__main__':
    main()
