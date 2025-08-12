# Scraping client blogs for published articles

## Run the script

### Windows command line

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
python scrape.py
```

### Linux

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
sudo $(which playwright) install-deps
python scrape.py
```

## How the script works

It uses Playwright to open a headless browser and scrape web pages.
If the website changes significantly, the scraper will break but it can be fixed by updating the details in `scraper_config.py` - see Setup section below.

NOTE: Some sites have anti scraping measures so can't run a headless browser. Akamai is one of these. A browser window will open up in this case.

1. Goes to a specified web page
2. Looks to see if there's a "Load more"-type button and clicks it until all posts are loaded.
3. Finds the <a> links for each post via a CSS selector or a Playwright selector.
   e.g. 'a[class*="blog_entry_card_card"]' is a CSS selector that will find all the <a>'s with a class that contains the text "blog_entry_card_card". So it will capture class names that change regularly like "blog_entry_card_card_jP5v"
4. Finds some other related info for each <a> like the URL it links to, title, date published
5. Saves to a .csv file

## Setup

- Enter the correct details in `scraper_config.py` - a developer can help work out what the selectors should be.
- The "url" needs to be the URL of a page with all the blog posts on it. Not a page that only has 3 sample posts on it. Click through until you get to a page with all the posts on it
- Or if they're organized by category you can scrape each category separately by having a config section for each URL that needs crawling.
