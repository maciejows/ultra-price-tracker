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

def get_data_from_url(url):
    scrap = UpcScrapper()
    if 'euro.com.pl' in url:
        return scrap.euro(url)
    if 'morele.net' in url:
        return scrap.morele(url)
    if 'x-kom.pl' in url:
        return scrap.xkom(url)
    if 'mediaexpert.pl' in url:
        return scrap.mediaexpert(url)
    if 'mediamarkt.pl' in url:
        return scrap.mediamarkt(url)
    if 'komputronik.pl' in url:
        return scrap.komputronik(url)
    if 'neo24.pl' in url:
        return scrap.neo24(url)

def get_pages(name):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    euro = multiprocessing.Process(target=search_euro, args=(name, data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=search_mediaexpert, args=(name, data_dict))
    mediaexpert.start()
    mediamarkt = multiprocessing.Process(target=search_mediamarkt, args=(name, data_dict))
    mediamarkt.start()
    neo24 = multiprocessing.Process(target=search_neo24, args=(name, data_dict))
    neo24.start()
    morele = multiprocessing.Process(target=search_morele, args=(name, data_dict))
    morele.start()
    komputronik = multiprocessing.Process(target=search_komputronik, args=(name, data_dict))
    komputronik.start()

    euro.join()
    mediaexpert.join()
    mediamarkt.join()
    neo24.join()
    morele.join()
    komputronik.join()
    print("all data covered")
    pages = data_dict
    return pages


def scrap_all_url(url):
    data = get_data_from_url(url)
    print(data['item'])
    pages = get_pages(data['item'])
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    print(str(pages['neo24']))
    print("starting multithreaded parsing")
    #print(pages)
    euro = multiprocessing.Process(target=sp.euro, args=(str(pages['euro']), data['item'], data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=sp.mediaexpert, args=(str(pages['mediaexpert']), data['item'], data_dict))
    mediaexpert.start()
    mediamarkt = multiprocessing.Process(target=sp.mediamarkt, args=(str(pages['mediamarkt']), data['item'], data_dict))
    mediamarkt.start()
    neo24 = multiprocessing.Process(target=sp.neo24, args=(str(pages['neo24']), data['item'], data_dict))
    neo24.start()
    morele = multiprocessing.Process(target=sp.morele, args=(str(pages['morele']), data['item'], data_dict))
    morele.start()
    komputronik = multiprocessing.Process(target=sp.morele, args=(str(pages['komputronik']), data['item'], data_dict))
    komputronik.start()

    euro.join()
    mediaexpert.join()
    mediamarkt.join()
    neo24.join()
    morele.join()
    komputronik.join()

    return data_dict


def search_euro(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.euro.com.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    print("euro - done")
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
      WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[13]/div[2]/div[5]/div[1]')))
      print("Page is ready!")
   except TimeoutException:
      print("The parameter was not find!")
      #print(driver.current_url)
      return_dict['mediaexpert'] = driver.current_url
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'm-offerBox_content clearfix')))
        print("Page is ready!")
    except TimeoutException:
        print("The parameter was not find!")
        # print(driver.current_url)
        return_dict['mediamarkt'] = driver.current_url
        return
    page = driver.page_source
    driver.close()
    print("mm - done")
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
    print("xkom - done")
    return page


def search_komputronik(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://komputronik.pl")
    input_element = driver.find_element_by_xpath('//input[@type="text"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 2  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-entry2 ')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return None
    page = driver.page_source
    driver.close()
    print("kom - done")
    return_dict['komputronik'] = page


def search_neo24(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://neo24.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Wpisz czego szukasz"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 10  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.ID, 'listingContent')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return_dict['neo24'] = None
        return
    page = driver.page_source
    driver.close()
    print("neo - done")
    return_dict['neo24'] = page

def get_page_neo24(url):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'productShopCss-neo24-product__price-12m')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return None
    page = driver.page_source
    # driver.close()
    return page

def search_morele(search_for, return_dict):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://morele.net")
    input_element = driver.find_element_by_xpath('//input[@name="search"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    print("morele - done")
    return_dict['morele'] = page



if __name__ == "__main__":
    #scrap = UpcScrapper()
    #parser = UpcParser()
    print(scrap_all_url("https://www.euro.com.pl/telefony-komorkowe/apple-iphone-pro-11-64gb-srebrny.bhtml"))
    #print(scrap.mediamarkt("https://mediamarkt.pl/rtv-i-telewizory/telewizor-philips-55pus6554-12"))
    #print(scrap.morele("https://www.morele.net/sluchawki-steelseries-arctis-1-61427-5938473/"))
    #print(scrap.komputronik("https://www.komputronik.pl/product/688817/huawei-matebook-x-pro-2020-green.html"))
    #print(scrap.neo24Scraper(get_page_neo24('https://www.neo24.pl/philips-55-55pus6704-uhd.html')))
    #print(scrap.euro("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
    #print(scrap.mediaexpert("https://www.mediaexpert.pl/telewizory-i-rtv/telewizory/telewizor-tcl-led-50ep680x1"))
    #print(scrap.xkom("https://www.x-kom.pl/p/423390-narzedzie-serwisowe-sieciowe-phanteks-toolkit-zestaw-narzedzi.html"))
    #print(scrap.neo24(get_page_neo24("https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"), "https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"))
    #print(search_mediamarkt("aoc"))
