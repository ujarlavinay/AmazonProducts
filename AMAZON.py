import requests
from bs4 import BeautifulSoup
import csv


def scrape_product_listings(url, num_pages=20):
    data = []
    for page in range(1, num_pages + 1):
        page_url = f"{url}&page={page}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        

    return data


def scrape_individual_product_page(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_details = {
        
    }

    return product_details

def export_to_csv(data, filename="output.csv"):
    header = ["Product Name", "Product Price", "Rating", "Number of Reviews", "Description", "ASIN", "Product Description", "Manufacturer"]
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(data)

# Main 
if __name__ == "__main__":

    amazon_url = "https://www.amazon.in/s?k=bags&crid=2M096C6104MLT&gid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg1"
    
    product_data = scrape_product_listings(amazon_url)

    for product in product_data:
        product_url = product["Product URL"]
        product_details = scrape_individual_product_page(product_url)
        product.update(product_details)

    export_to_csv(product_data)
