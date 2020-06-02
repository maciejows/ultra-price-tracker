import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

def parser(page, product_code):
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all("div", {'class': ''})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        tag_name = data.find('h2', {'class': ''})
        name = tag_name.text.strip()
        # print(name)
        if name.lower() == product_code.lower():
            link = 'www.morele.net' + tag_name.a['href'].strip()
            tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
            price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
            return [name, price, link]
        else:
            continue
    return False

if __name__ == "__main__":

    page = open('neo24List.html', encoding='utf-8')
    print(parser(page))