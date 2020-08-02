import ast

import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import multiprocessing
from scraper.parser import UpcParser
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

def search_mediaexpert(search_for):
   driver = webdriver.Chrome(options=options)
   driver.get("https://www.mediaexpert.pl")
   driver.set_window_size(1920, 1080)
   input_element = driver.find_element_by_css_selector('div.c-search_input').find_element_by_tag_name('input')
   input_element.send_keys(search_for)
   input_element.send_keys(Keys.ENTER)
   delay = 5 # seconds
   try:
      WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[13]/div[2]/div[5]/div[1]')))
      print("Page is ready!")
   except TimeoutException:
      print("Parameter was not find!")
      print(driver.current_url)
      return driver.current_url
   page = driver.page_source
   driver.close()
   return page


def mediaexpert(page, product_code):
   if page is None or page.startswith("https://www.mediaexpert.pl"):
      scrap = UpcScrapper()
      return scrap.mediaexpert(page)
   soup = BeautifulSoup(page, 'html.parser')
   product_list = soup.find_all("div", {'class': 'c-grid_col is-grid-col-1'})
   for product in product_list:
      data = BeautifulSoup(str(product), 'lxml')
      tag_name = data.find('a', {'class': 'a-typo is-secondary'})
      #print(tag_name)
      name = tag_name.text.replace("\xa0", "").replace("zł", "").replace('\n','')
      #print(name)
      if product_code.lower() in name.lower():
         link = 'www.mediaexpert.pl' + tag_name['href']
         tag_price = data.find('span', {'class': 'a-price_price'})
         price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
         img = 'null'
         data_set = {'item': name, 'price': price, 'link': link}
         return data_set
      else:
         continue
   return None


if __name__ == '__main__':
   lala = 'Telewizor PHILIPS LED'
   print(mediaexpert(search_mediaexpert(lala), lala))