from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scraper.scrpr import upcScrapper

searchingPhrase = "PHILIPS 55PUS6554/12"


def searchEuro(search_for):
    driver = webdriver.Chrome()
    driver.get("https://www.euro.com.pl")
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page

def searchME(search_for):
    driver = webdriver.Chrome()
    driver.get("https://www.mediaexpert.pl")
    input_element = driver.find_element_by_css_selector('div.c-search_input').find_element_by_tag_name('input')
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page

def searchMM(search_for):
    driver = webdriver.Chrome()
    driver.get("https://mediamarkt.pl")
    input_element = driver.find_element_by_id("query_querystring")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


if __name__ == "__main__":
    scrap = upcScrapper()
    #print(scrap.euroParser(searchEuro(searchingPhrase), searchingPhrase))

    print(searchMM(searchingPhrase), searchingPhrase)
    #print(scrap.euroScraper("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
    #print(scrap.meScraper("https://www.mediaexpert.pl/telewizory-i-rtv/telewizory/telewizor-tcl-led-50ep680x1"))
    #print(scrap.mmScraper("https://mediamarkt.pl/komputery-i-tablety/laptop-apple-macbook-air-13-mqd32ze-a-i5-8gb-128gb-ssd-macos"))
    #print(scrap.xkScraper("https://www.x-kom.pl/p/423390-narzedzie-serwisowe-sieciowe-phanteks-toolkit-zestaw-narzedzi.html"))
