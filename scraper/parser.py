import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup


# BeautifulSoup - for parsing HTML.


class UpcParser:
    def euro_parser(self, page, entered_expression):
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': 'product-box js-UA-product'})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('h2', {'class': 'product-name'})
            name = tag_name.text.strip()
            # print(name)
            if entered_expression.lower() in name.lower():
                link = 'www.euro.com.pl' + tag_name.a['href'].strip()
                tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
                price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
                return [name, price, link]
            else:
                continue
        return False

    def me_parser(self, page, entered_expression):
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': ''})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('h2', {'class': ''})
            name = tag_name.text.strip()
            # print(name)
            if name.lower() == entered_expression.lower():
                link = 'www.euro.com.pl' + tag_name.a['href'].strip()
                tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
                price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
                return [name, price, link]
            else:
                continue
        return False

    def neo24_parser(self, page, product_code):
        if page is None:
            return None
        soup = BeautifulSoup(page, 'lxml')
        product_list = soup.select('div[class*="listingItemCss-neo24-item"]')
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            name_tag = data.select('a[class*="listingItemCss-neo24-nameLink"]')
            name = name_tag[0].contents[0]
            if product_code in name:
                link = "https://www.neo24.pl" + name_tag[0].attrs['href']
                img = data.select('img[class*="slideCss-lazy"]')[0].attrs['src']
                price = data.select('div[class*="specialPriceFormatterCss-neo24"]')[0].contents[0].contents[0].strip()
                data_set = {'item': name, 'price': price, 'link': link, 'img': img}
                return data_set
            else:
                continue
        return None
