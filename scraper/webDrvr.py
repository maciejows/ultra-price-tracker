from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searchingPhrase="TCL 50EP640"

def searchEuro(searchFor):
    price=0.00
    driver = webdriver.Chrome()
    driver.get("https://www.euro.com.pl")
    inputElement = driver.find_element_by_id("keyword")
    inputElement.send_keys(searchingPhrase)
    inputElement.send_keys(Keys.ENTER)

    return price

if __name__ == "__main__":
    searchEuro(searchingPhrase)