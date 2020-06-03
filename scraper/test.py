import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

class test:
    def __init__(self):
        pass
    def cleanText(self, text):
        return text.strip().replace('\n', '').replace('\t', '').replace(
            '  ', '').replace("\xa0", "")


    def cleanPrice(self, text):
        return text.replace('\n', '').replace('\t', '').replace(
            ' ', '').replace("\xa0", "").replace("zł", "").replace("zl", "").replace(",", ".")

    def parser(self, page, product_code):
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all('div', class_='m-offerBox_content clearfix')
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            #print(data)
            product_data = data.find('a', {'class': 'js-product-name'})
            #print(product_data)
            name = self.cleanText(product_data['title'])
            print(name)
            if product_code.lower() in name.lower():
                link = "https://mediamarkt.pl" + product_data['href']
                #print(link)
                price = self.cleanPrice(product_data['data-offer-price'])
                #print(price)
                data_set = {'item': name, 'price': price, 'link': link}
                return data_set
            else:
                continue
        return False

if __name__ == "__main__":
    testing = test()
    page = open('result.html', encoding='utf-8')
    print(testing.parser(page, 'AG251FG'))