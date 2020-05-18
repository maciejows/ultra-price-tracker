from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from scraper.scrpr import upcScrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

searchingPhrase = "PHILIPS 55"
options = Options()
options.add_argument('--headless')

def search_euro(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.euro.com.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_mediaexpert(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.mediaexpert.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_css_selector('div.c-search_input').find_element_by_tag_name('input')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_mediamarkt(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://mediamarkt.pl")
    driver.set_window_size(1920, 1080)
    input_element = driver.find_element_by_id("query_querystring")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_xkom(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://x-kom.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Czego szukasz?"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_komputronik(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://komputronik.pl")
    input_element = driver.find_element_by_xpath('//input[@type="text"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


def search_neo24(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://neo24.pl")
    input_element = driver.find_element_by_xpath('//input[@placeholder="Wpisz czego szukasz"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    delay = 5  # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'listingContent')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        return None

    page = driver.page_source
    # driver.close()
    return page


def search_morele(search_for):
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://morele.net")
    input_element = driver.find_element_by_xpath('//input[@name="search"]')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    # driver.close()
    return page


if __name__ == "__main__":
    scrap = upcScrapper()
    # print(scrap.euroParser(search_euro(searchingPhrase), searchingPhrase))
    print(scrap.neo24Parser(search_neo24(searchingPhrase)))
    # print(scrap.euroScraper("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
    # print(scrap.meScraper("https://www.mediaexpert.pl/telewizory-i-rtv/telewizory/telewizor-tcl-led-50ep680x1"))
    # print(scrap.mmScraper("https://mediamarkt.pl/komputery-i-tablety/laptop-apple-macbook-air-13-mqd32ze-a-i5-8gb-128gb-ssd-macos"))
    # print(scrap.xkScraper("https://www.x-kom.pl/p/423390-narzedzie-serwisowe-sieciowe-phanteks-toolkit-zestaw-narzedzi.html"))
