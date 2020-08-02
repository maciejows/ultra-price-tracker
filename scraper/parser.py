import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup


# BeautifulSoup - for parsing HTML.
# return_dict - [euro, mediaexpert, neo24, morele, komputronik, mediamarkt]
from scraper.scrpr import UpcScrapper


class UpcParser:

    def cleanText(self, text):
        return text.strip().replace('\n', '').replace('\t', '').replace(
                '  ', '').replace("\xa0", "")

    def cleanPrice(self, text):
        return text.replace('\n', '').replace('\t', '').replace(
            ' ', '').replace("\xa0", "").replace("zł", "").replace("zl", "").replace(",", ".")

    def euro(self, page, product_code, return_dict):
        print("euro: " + str(len(page)))
        if page is None:
            return_dict['euro'] = None
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': 'product-box js-UA-product'})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('h2', {'class': 'product-name'})
            name = self.cleanText(tag_name.text)
            # print(name)
            if product_code.lower() in name.lower():
                link = 'www.euro.com.pl' + tag_name.a['href'].strip()
                tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
                price = self.cleanPrice(tag_price.text)
                img='null'
                data_set = {'item': name, 'price': price, 'link': link, 'img': img}
                return_dict['euro'] = data_set
                return
            else:
                continue
        return_dict['euro'] = None

    def mediaexpert(page, product_code):
        if page is None or page.startswith("https://www.mediaexpert.pl"):
            scrap = UpcScrapper()
            return scrap.mediaexpert(page)
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': 'c-grid_col is-grid-col-1'})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('a', {'class': 'a-typo is-secondary'})
            # print(tag_name)
            name = tag_name.text.replace("\xa0", "").replace("zł", "").replace('\n', '')
            # print(name)
            if product_code.lower() in name.lower():
                link = 'www.mediaexpert.pl' + tag_name['href']
                tag_price = data.find('span', {'class': 'a-price_price'})
                price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
                img = 'null'
                data_set = {'item': name, 'price': price, 'link': link}
                return data_set
            else:
                continue
        return None

    def neo24(self, page, product_code, return_dict):
        print("neo: " + str(len(page)))
        if page is None:
            return_dict['neo24'] = None
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
                return_dict['neo24'] = data_set
                return
            else:
                continue
        return_dict['neo24'] = None

    def morele(self, page, product_code, return_dict):
        print("morele: " + str(len(page)))
        if page is None:
            return_dict['morele'] = None
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': 'cat-product card'})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            # print(data)
            product_data = data.find('div', {'class': 'cat-product card'})
            # print(product_data)
            name = product_data.attrs['data-product-name']
            # print(name)
            if product_code.lower() in name.lower():
                tag_link = data.find('a', {'class': 'cat-product-image productLink'})
                # print(tag_link)
                link = 'https://www.morele.net' + tag_link['href']
                # print(link)
                price = product_data['data-product-price']
                # print(price)
                img = tag_link.img['src']
                data_set = {'item': name, 'price': price, 'link': link, 'img': img}
                return_dict['morele'] = data_set
                return
            else:
                continue
        return_dict['morele'] = None

    def komputronik(self, page, product_code, return_dict):
        print("komp: " + str(len(page)))
        if page is None:
            return_dict['komputronik'] = None
        soup = BeautifulSoup(page, 'html.parser')
        product_list = soup.find_all("div", {'class': ''})
        for product in product_list:
            data = BeautifulSoup(str(product), 'lxml')
            tag_name = data.find('h2', {'class': ''})
            name = tag_name.text.strip()
            # print(name)
            if name.lower() == product_code.lower():
                link = 'www.komputronik.pl' + tag_name.a['href'].strip()
                tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
                price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
                img = 'null'
                data_set = {'item': name, 'price': price, 'link': link, 'img': img}
                return_dict['komputronik'] = data_set
                return
            else:
                continue
        return_dict['komputronik'] = None

    def mediamarkt(self, page, product_code, return_dict):
        print("mm: " + str(len(page)))
        if page is None:
            return_dict['mediamarkt'] = None
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
                return_dict['mediamarkt'] = data_set
                return
            else:
                continue
        return_dict['mediamarkt'] = None