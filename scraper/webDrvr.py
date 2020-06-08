from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from scraper.scrpr import UpcScrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

searchingPhrase = "50ep640"
options = Options()
options.add_argument('--headless')

def search_euro(search_for):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.euro.com.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_mediaexpert(search_for):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.mediaexpert.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_css_selector('div.c-search_input').find_element_by_tag_name('input')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_mediamarkt(search_for):
    driver = webdriver.Chrome(options=options)
    driver.get("https://mediamarkt.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("query_querystring")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_xkom(search_for):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://x-kom.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Czego szukasz?"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_komputronik(search_for):
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
    return page


def search_neo24(search_for):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://neo24.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Wpisz czego szukasz"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 2  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'listingContent')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return None
    page = driver.page_source
    driver.close()
    return page

def get_page_neo24(url):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    delay = 2  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'productShopCss-neo24-product__price-12m')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return None
    page = driver.page_source
    # driver.close()
    return page

def search_morele(search_for):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://morele.net")
    input_element = driver.find_element_by_xpath('//input[@name="search"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page

if __name__ == "__main__":
    #scrap = UpcScrapper()
    #print(scrap.mediamarkt("https://mediamarkt.pl/rtv-i-telewizory/telewizor-philips-55pus6554-12"))
    #print(scrap.morele("https://www.morele.net/sluchawki-steelseries-arctis-1-61427-5938473/"))
    #print(scrap.komputronik("https://www.komputronik.pl/product/688817/huawei-matebook-x-pro-2020-green.html"))
    #print(scrap.neo24Scraper(get_page_neo24('https://www.neo24.pl/philips-55-55pus6704-uhd.html')))
    #print(scrap.euro("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
    #print(scrap.mediaexpert("https://www.mediaexpert.pl/telewizory-i-rtv/telewizory/telewizor-tcl-led-50ep680x1"))
    #print(scrap.xkom("https://www.x-kom.pl/p/423390-narzedzie-serwisowe-sieciowe-phanteks-toolkit-zestaw-narzedzi.html"))
    #print(scrap.neo24(get_page_neo24("https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"), "https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"))
    print(search_mediamarkt("aoc"))
