import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
from scraper import webdrvr as wd
import lxml

# BeautifulSoup - for parsing HTML.


class UpcScrapper:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    # header-HTTP headers provide additional parameters to HTTP transactions.
    # By sending the appropriate HTTP headers, one can access the response data in a different format.
    def cleanText(self, text):
        return text.strip().replace('\n', '').replace('\t', '').replace(
                '  ', '').replace("\xa0", "")

    def clean_price(self, text):
        return text.replace('\n', '').replace('\t', '').replace(
            ' ', '').replace("\xa0", "").replace("zł", "").replace("zl", "").replace(",", ".")

    def fix_url(self, url):
        if url is None or url == 404:
            return None
        url = str(url)
        if url.startswith("www"):
            return "http://"+url
        else:
            return url

    def euro(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        # result - this is the response object returned by the get method.
        # Here, we pass the base_url and header as parameters.
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(self.clean_price(soup.find("div", {'class': 'price-normal selenium-price-normal'}).text))
            name = self.cleanText(soup.find("h1", {'class': 'selenium-KP-product-name'}).text)
            link = base_url
            img = soup.find("a", {'id': 'big-photo'}).attrs['href']
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return data_set
        else:
            return result.status_code

    def mediaexpert(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(self.clean_price(soup.find("span", {'class': 'a-price_price'}).text))
            name = self.cleanText(soup.find("h1", {'class': 'a-typo is-primary'}).text)
            link = base_url
            img = 'https://www.mediaexpert.pl' + soup.find("div", {'class': 'c-offerBox_galleryItem'}).contents[0]['data-src']
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return data_set
        else:
            return result.status_code

    def mediamarkt(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(self.clean_price(soup.find("span", {'itemprop': 'price'}).text))
            name = self.cleanText(soup.find("h1", {'class': 'm-typo m-typo_primary'}).text)
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def xkom(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(self.clean_price(soup.find("meta", {'property': 'product:price:amount'})['content']))
            name = self.cleanText(soup.find("div", {'class': 'col-xs-12 product-detail-impression'})['data-product-name'])
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def neo24(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        page = wd.get_page_neo24(base_url)
        soup = BeautifulSoup(page, 'html.parser')
        # file = open("result.html", 'w')
        # file.write(page)
        # file.close()
        name = self.cleanText(soup.select('h1[class*="productFullDetailDesktopCss-neo24-productName"]')[0].contents[0].string)
        decimal = "0." + soup.select('div[class*="productShopCss-neo24-sp__fraction"]')[0].contents[0]
        price = float(self.clean_price(soup.select('div[class*="productShopCss-neo24-sp__root"]')[0].contents[0].string)) + float(decimal)
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return data_set

    def morele(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = float(self.clean_price(soup.find("div", {'id': 'product_price_brutto'}).text))
            name = self.cleanText(soup.find("h1", {'class': 'prod-name'}).text)
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code

    def komputronik(self, base_url):
        base_url = self.fix_url(base_url)
        if base_url is None:
            return None
        result = requests.get(base_url, headers=self.header)
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            price = self.clean_price((soup.find("span", {'class': 'price'})).contents[1].text)
            name = soup.find("title").text
            name = self.cleanText(name[0:name.find("|")].strip())
            link = base_url
            data_set = {'item': name, 'price': price, 'link': link}
            return data_set
        else:
            return result.status_code
