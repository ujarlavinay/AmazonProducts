# Amazon Product Scraper

This is a Python script for scraping product listings and individual product details from Amazon's website.

## Overview

This script is designed to scrape product listings from Amazon based on a search query and then gather detailed information about each individual product. The scraped data is exported to a CSV file for analysis.

## Features

- Scrapes product listings from Amazon based on a search query.
- Extracts product URLs, names, prices, ratings, and review counts.
- Scrapes individual product pages to extract description, ASIN, product description, and manufacturer.
- Exports all collected data to a CSV file for further analysis.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## How to Use

1. Clone or download the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Update the `amazon_url` variable in the main script with the desired Amazon search URL.
4. Run the script using `python script_name.py`.
5. The scraped data will be saved in the `output.csv` file in the same directory

Feel free to customize this README template to match your project. Add more information, instructions, and explanations as needed.
