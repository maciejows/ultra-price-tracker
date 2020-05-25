import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup


# BeautifulSoup - for parsing HTML.


class UpcScrapper:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    # header-HTTP headers provide additional parameters to HTTP transactions.
    # By sending the appropriate HTTP headers, one can access the response data in a different format.

    def euro(self, base_url):
        result = requests.get(base_url, headers=self.header)
        # result - this is the response object returned by the get method.
        # Here, we pass the base_url and header as parameters.
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("div", {'class': 'price-normal selenium-price-normal'}).text.strip().replace("\xa0", "").replace("zł", ""))
            name = soup.find("h1", {'class': 'selenium-KP-product-name'}).text.replace('\n', '').replace('\t', '')
            link = base_url
            img = soup.find("a", {'id': 'big-photo'}).attrs['href']
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return data_set
        else:
            return result.status_code

    def mediaexpert(self, base_url):
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("span", {'class': 'a-price_price'}).text.replace(" ", ""))
            name = soup.find("h1", {'class': 'a-typo is-primary'}).text.replace('\n', '').replace('\t', '')
            link = base_url
            img = 'https://www.mediaexpert.pl' + soup.find("div", {'class': 'c-offerBox_galleryItem'}).contents[0]['data-src']
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return data_set
        else:
            return result.status_code

    def mediamarkt(self, base_url):
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("span", {'itemprop': 'price'}).text.replace(" ", ""))
            name = soup.find("h1", {'class': 'm-typo m-typo_primary'}).text.replace('\n', '').replace('\t', '').replace('  ', '')
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def xkom(self, base_url):
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("meta", {'property': 'product:price:amount'})['content'])
            name = soup.find("div", {'class': 'col-xs-12 product-detail-impression'})['data-product-name']
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def neo24(self, page, base_url):
        if page is None:
            return None
        soup = BeautifulSoup(page, 'lxml')
        name = soup.select('h1[class*="productFullDetailDesktopCss-neo24-productName"]')[0].contents[0].string
        decimal = "0." + soup.select('div[class*="productShopCss-neo24-sp__fraction"]')[0].contents[0]
        price = float(soup.select('div[class*="productShopCss-neo24-sp__root"]')[0].contents[0].string.replace(' ', '')) + float(decimal)
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return data_set

    def morele(self, base_url):
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("div", {'id': 'product_price_brutto'}).text.replace("zł", "").replace(' ', ''))
            name = soup.find("h1", {'class': 'prod-name'}).text.replace('\n', '').replace('\t', '').replace(
                '  ', '')
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def komputronik(self, base_url):
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(soup.find("div", {'id': 'product_price_brutto'}).text.replace("zł", "").replace(' ', ''))
            name = soup.find("h1", {'class': 'prod-name'}).text.replace('\n', '').replace('\t', '').replace(
                '  ', '')
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code