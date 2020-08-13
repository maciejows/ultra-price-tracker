from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import multiprocessing
import scraper.parser as sp
from scraper.scrpr import UpcScrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

searchingPhrase = "50ep640"
options = Options()
options.add_argument('--headless')

def search_euro(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.euro.com.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    #print("euro - done")
    return_dict['euro'] = page


def search_mediaexpert(search_for, return_dict):
   driver = webdriver.Chrome(options=options)
   driver.get("https://www.mediaexpert.pl")
   driver.set_window_size(1920, 1080)
   input_element = driver.find_element_by_css_selector('div.c-search_input').find_element_by_tag_name('input')
   input_element.send_keys(search_for)
   input_element.send_keys(Keys.ENTER)
   delay = 5 # seconds
   try:
      WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.c-offerBox.is-wide.is-available')))
      #print("Page is ready! ME")
   except TimeoutException:
      #print("The parameter was not find! ME")
      #print(driver.current_url)
      return_dict['mediaexpert'] = driver.current_url
      driver.close()
      return
   page = driver.page_source
   driver.close()
   return_dict['mediaexpert'] = page


def search_mediamarkt(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.get("https://mediamarkt.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("query_querystring")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="js-mainWrapper"]/main/div[6]/div[5]/div[2]/div')))
        #print("Page is ready! MM")
    except TimeoutException:
        #print("The parameter was not find! MM")
        # print(driver.current_url)
        return_dict['mediamarkt'] = driver.current_url
        driver.close()
        return
    page = driver.page_source
    driver.close()
    #print("mm - done")
    return_dict['mediamarkt'] = page


def search_xkom(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://x-kom.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Czego szukasz?"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    #print("xkom - done")
    return page


def search_komputronik(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://komputronik.pl")
    input_element = driver.find_element_by_xpath('//input[@type="text"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-entry2 ')))
        #print("Page is ready! Kom")
    except TimeoutException:
        #print("The parameter was not find!  Kom")
        return_dict['komputronik'] = driver.current_url
        driver.close()
        return
    page = driver.page_source
    driver.close()
    return_dict['komputronik'] = page


def search_neo24(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://neo24.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Wpisz czego szukasz"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.ID, 'listingContent')))
        #print("Page is ready!")
    except TimeoutException:
        #print("The parameter was not find! ")
        return_dict['neo24'] = driver.current_url
        driver.close()
        return
    page = driver.page_source
    driver.close()
    #print("neo - done")
    return_dict['neo24'] = page


def get_page_neo24(url):
    try:
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        driver.get(url)
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'productShopCss-neo24-product__price-12m')))
            #print("Page is ready!")
        except TimeoutException:
            driver.close()
            #print("The parameter was not find!")
            return None
        page = driver.page_source
        driver.close()
        return page
    except:
        return None

def search_morele(search_for, return_dict):
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
        # print("Page is ready! Morle")
    except TimeoutException:
        # print("The parameter was not find!")
        driver.close()
        return_dict['morele'] = None
    page = driver.page_source
    driver.close()
    # print("morele - done")
    return_dict['morele'] = page

