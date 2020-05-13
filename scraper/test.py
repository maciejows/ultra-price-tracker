import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup

def euroCheck(entered_expression):
    page = open('result.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(page.read(), 'html.parser')
    product_list = soup.find_all("div", {'class': 'product-box js-UA-product'})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        tag_name = data.find('h2', {'class': 'product-name'})
        name = tag_name.text.strip()
        if name.lower() == entered_expression:
            link = 'https://www.euro.com.pl' + tag_name.a['href'].strip()
            tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
            price = tag_price.text.strip().replace("\xa0","").replace("zł","")
            return [name, price, link]
        else:
            continue
    return False

if __name__ == "__main__":
    entered_expression = "tcl 50ep640"
    print(euroCheck(entered_expression))