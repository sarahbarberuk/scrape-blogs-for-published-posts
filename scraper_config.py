SCRAPER_CONFIGS = {
    
    "appsmith": {
        "display_name": "Appsmith",
        "url": "https://www.appsmith.com/blog",
        "post_selector": "a[href^='/blog/']",
        "title_selectors": [
            "h2.leading-tight span",                               
            "span.text-base.font-medium.leading-tight"  
        ],
        "date_selectors": [
            "h2.font-display ~ div time", 
            "div.text-xs.text-primary-light-500\\/70"
        ],
        "author_selectors": [
            "h2.font-display ~ div .text-ellipsis.text-sm.font-medium",
            "div.text-ellipsis.text-sm.font-medium"
        ],
        "base_url": "https://www.appsmith.com",
        "needs_click_to_load_more": True,
        "load_more_selector": 'button:has-text("Load more")',
        "load_more_delay": 2000,
        "wait_until": "domcontentloaded"
    }
}