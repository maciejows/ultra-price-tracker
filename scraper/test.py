import ast

import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re

from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import multiprocessing

from scraper import parser
from scraper.scrpr import UpcScrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
import queue
import threading
import time

options = Options()
options.add_argument('--headless')


def search_neo24(search_for):
   driver = webdriver.Chrome(options=options)
   driver.set_window_size(1920, 1080)
   driver.get("https://morele.net")
   input_element = driver.find_element_by_xpath('//input[@name="search"]')
   input_element.send_keys(search_for)
   input_element.send_keys(Keys.ENTER)
   delay = 3  # seconds
   try:
      WebDriverWait(driver, delay).until(
         EC.presence_of_element_located((By.CLASS_NAME, 'cat-list-products')))
      print("Page is ready!")
   except TimeoutException:
      print("The parameter was not find!")
      return None
   page = driver.page_source
   driver.close()
   print("morele - done")
   return page


if __name__ == '__main__':
   manager = multiprocessing.Manager()
   data_dict = manager.dict()
   #file = open("result.html", 'r')
   #data = file.read()
   #file.close()
   parser.morele(search_neo24("Apple iPhone 11 Pro 64GB (srebrny)"), "Apple iPhone 11 Pro 64GB (srebrny)", data_dict)
   #scrap = UpcScrapper()
   #print(scrap.mediamarkt("https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-11-pro-max-64gb-zloty-mwhg2pm-a?querystring=Smartfon%20APPLE%20iPhone%2011%20Pro%20Max%2064GB%20Złoty"))
   print(data_dict)