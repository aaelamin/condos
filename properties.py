
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def load_page(driver, city, type, page):
    url = f"https://condos.ca/{city}/condos-for-{type}?page={page}"
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    return soup


def main():
    driver = webdriver.Chrome()
    city = "Toronto"
    type = "Rent"
    page = 3
    soup = load_page(driver, city, type, page)
main()