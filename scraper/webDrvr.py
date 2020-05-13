from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scraper.scrpr import upcScrapper

searchingPhrase = "TCL 50EP640"


def searchEuro(search_for):
    driver = webdriver.Chrome()
    driver.get("https://www.euro.com.pl")
    input_element = driver.find_element_by_id("keyword")
    input_element.send_keys(search_for)
    input_element.send_keys(Keys.ENTER)
    page = driver.page_source
    driver.close()
    return page


if __name__ == "__main__":
    scrap = upcScrapper()
    #print(scrap.euroParser(searchEuro(searchingPhrase), searchingPhrase))
    print(scrap.euroScraper("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
