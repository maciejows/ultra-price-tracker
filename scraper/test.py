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
#options.add_argument('--headless')


def search_neo24(search_for):
   driver = webdriver.Chrome(options=options)
   driver.set_window_size(1920, 1080)
   driver.get("https://komputronik.pl")
   input_element = driver.find_element_by_xpath('//input[@type="text"]')
   input_element.send_keys(search_for)
   input_element.send_keys(Keys.ENTER)
   delay = 3  # seconds
   try:
      WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-entry2 ')))
      print("Page is ready!")
   except TimeoutException:
      print("Loading took too much time!")
      url = driver.current_url
      driver.close()
      return url
   page = driver.page_source
   driver.close()
   print("kom - done")
   return page


if __name__ == '__main__':
   manager = multiprocessing.Manager()
   data_dict = manager.dict()
   file = open("result.html", 'r')
   data = file.read()
   file.close()
   parser.komputronik("https://www.komputronik.pl/product/657984/apple-iphone-11-pro-max-64gb-zloty.html", "Smartfon APPLE iPhone 11 Pro Max 64GB Gold", data_dict)
   print(data_dict)