import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup


# BeautifulSoup - for parsing HTML.


class upcScrapper:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    def euroParser(self, page, entered_expression):
        #print(entered_expression)
        #page = open('result.html', 'r', encoding='utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': 'product-box js-UA-product'})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('h2', {'class': 'product-name'})
            name = tag_name.text.strip()
            #print(name)
            if name.lower() == entered_expression.lower():
                link = 'www.euro.com.pl' + tag_name.a['href'].strip()
                tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
                price = tag_price.text.strip().replace("\xa0","").replace("zł","")
                return [name, price, link]
            else:
                continue
        return False

    def euroScraper(self, base_url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        # header-HTTP headers provide additional parameters to HTTP transactions.
        # By sending the appropriate HTTP headers, one can access the response data in a different format.
        result = requests.get(base_url, headers=header)
        # result - this is the response object returned by the get method.
        # Here, we pass the base_url and header as parameters.
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            return soup.find("div", {'class': 'price-normal selenium-price-normal'}).text.strip().replace("\xa0","").replace("zł","")
        else:
            return result.status_code
