# scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_products(url):
    """Scrape product information from BooksToScrape."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to load page")

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    # Update selectors based on BooksToScrape structure
    for product in soup.select(".product_pod"):
        name = product.h3.a["title"]
        price = product.select_one(".price_color").get_text(strip=True)
        rating = product.p["class"][1]  # Rating is stored as a class, e.g., "star-rating Three"
        
        products.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })

    return products

def save_to_csv(products, filename="products.csv"):
    """Save the scraped data to a CSV file."""
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
