
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import pandas as pd

def load_page( city, type, page):
    driver = webdriver.Chrome()
    url = f"https://condos.ca/{city}/condos-for-{type}?page={page}"
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    return soup

def containers(soup):
    div = soup.find_all('div', {'class':"styles___PreviewContent-sc-54qk44-3 kGcPgm"})
    return div

def main():
    city = input("Enter the city:\n")
    type = input("Condos for sale or rent:\n")
    soup = load_page(city, type, 1)
    listings = containers(soup)

main()
