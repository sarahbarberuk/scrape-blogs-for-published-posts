SCRAPER_CONFIGS = {

        "contentful": {
        "display_name": "Contentful",
        "url": "https://www.contentful.com/blog/category/guides/",
        "post_selector": 'a[class*="blog_entry_card_card"]',
        "title_selector": 'p[class*="card_with_image_title"]',
        "date_selector": 'p[class*="card_with_image_description"]',
        "base_url": "https://www.contentful.com",
        "needs_click_to_load_more": True,
        "load_more_selector": 'button:has-text("See more articles")',
        "load_more_delay": 2000,
        "wait_until": "networkidle"

    },
    "appsmith": {
        "display_name": "Appsmith",
        "url": "https://www.appsmith.com/blog",
        "post_selector": "a[href^='/blog/']",
        "title_selector": 'span.text-base.font-medium.leading-tight',
        "date_selector": 'div.text-xs.text-primary-light-500\\/70',
        "base_url": "https://www.appsmith.com",
        "needs_click_to_load_more": True,
        "load_more_selector": 'button:has-text("Load more")',
        "load_more_delay": 2000,
        "wait_until": "networkidle"

    },
    "stytch": {
        "display_name": "Stytch",
        "url": "https://stytch.com/blog/category/latest/",
        "post_selector": "a[class*='sc-a6d4489c-2']",                  
        "title_selector": "h3[class*='sc-3cfc3a4a-0']",                             
        "date_selector": "div[class*='sc-556084ac-0'] + div",  
        "base_url": "https://www.stytch.com",
        "needs_click_to_load_more": False,
        "wait_until": "domcontentloaded"

    }
}