import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup

from fuzzywuzzy import fuzz

# BeautifulSoup - for parsing HTML.
# return_dict - [euro, mediaexpert, neo24, morele, komputronik, mediamarkt]
from scraper.scrpr import UpcScrapper


def cleanText(text):
    return text.strip().replace('\n', '').replace('\t', '').replace(
            '  ', '').replace("\xa0", "")

def cleanPrice(text):
    return text.replace('\n', '').replace('\t', '').replace(
        ' ', '').replace("\xa0", "").replace("zł", "").replace("zl", "").replace(",", ".")

def euro(page, product_code, return_dict):
    print("euro: " + str(len(page)))
    if page is None:
        return_dict['euro'] = None
        return
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all("div", {'class': 'product-box js-UA-product'})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        tag_name = data.find('h2', {'class': 'product-name'})
        name = cleanText(tag_name.text)
        # print(name)
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        print(ratio)
        if ratio > 50:
            link = 'www.euro.com.pl' + tag_name.a['href'].strip()
            tag_price = data.find('div', {'class': 'price-normal selenium-price-normal'})
            price = cleanPrice(tag_price.text)
            img='null'
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return_dict['euro'] = data_set
            return
        else:
            continue
    return_dict['euro'] = None

def mediaexpert(page, product_code, return_dict):
    if page is None or page.startswith("https://www.mediaexpert.pl"):
        scrap = UpcScrapper()
        return_dict['mediaexpert'] = scrap.mediaexpert(page)
        return
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all("div", {'class': 'c-grid_col is-grid-col-1'})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        tag_name = data.find('a', {'class': 'a-typo is-secondary'})
        # print(tag_name)
        name = tag_name.text.replace("\xa0", "").replace("zł", "").replace('\n', '')
        # print(name)
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        print(ratio)
        if ratio > 50:
            link = 'www.mediaexpert.pl' + tag_name['href']
            tag_price = data.find('span', {'class': 'a-price_price'})
            price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
            return_dict['mediaexpert'] = {'item': name, 'price': price, 'link': link}
            return
        else:
            continue
    return_dict['mediaexpert'] = None

def neo24(page, product_code, return_dict):
    print("neo: " + str(len(page)))
    if page is None:
        return_dict['neo24'] = None
        return
    soup = BeautifulSoup(page, 'lxml')
    product_list = soup.select('div[class*="listingItemCss-neo24-item"]')
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        name_tag = data.select('a[class*="listingItemCss-neo24-nameLink"]')
        name = name_tag[0].contents[0]
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        print(ratio)
        if ratio > 50:
            link = "https://www.neo24.pl" + name_tag[0].attrs['href']
            img = data.select('img[class*="slideCss-lazy"]')[0].attrs['src']
            price = data.select('div[class*="specialPriceFormatterCss-neo24"]')[0].contents[0].contents[0].strip()
            data_set = {'item': name, 'price': price, 'link': link, 'img': img}
            return_dict['neo24'] = data_set
            return
        else:
            continue
    return_dict['neo24'] = None

def morele(page, product_code, return_dict):
    print("morele: " + str(len(page)))
    if page is None:
        return_dict['morele'] = None
        return
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all("div", {'class': 'cat-product card'})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        # print(data)
        product_data = data.find('div', {'class': 'cat-product card'})
        # print(product_data)
        name = product_data.attrs['data-product-name']
        # print(name)
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        print(ratio)
        if ratio > 50:
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

def komputronik(page, product_code, return_dict):
    #print("komp: " + str(len(page)))
    if page is None or page.startswith("https://www.komputronik.pl"):
        scrap = UpcScrapper()
        return_dict['komputronik'] = scrap.komputronik(page)
        return
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all("li", {'class': 'product-entry2'})
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        tag_name = data.find('a', {'class': 'blank-link at-product-name-0'})
        name = tag_name.text.strip()
        #print(name)
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        if ratio > 60:
            link = 'www.komputronik.pl' + tag_name['href'].strip()
            tag_price = data.find('span', {'class': 'proper at-gross-price-0'})
            price = tag_price.text.strip().replace("\xa0", "").replace("zł", "")
            data_set = {'item': name, 'price': price, 'link': link}
            return_dict['komputronik'] = data_set
            return
        else:
            continue
    return_dict['komputronik'] = None

def mediamarkt(page, product_code, return_dict):
    if page is None or page.startswith("https://www.mediamarkt.pl") or page.startswith("https://mediamarkt.pl"):
        scrap = UpcScrapper()
        return_dict['mediamarkt'] = scrap.mediamarkt(page)
        return
    soup = BeautifulSoup(page, 'html.parser')
    product_list = soup.find_all('div', class_='m-offerBox_content clearfix')
    for product in product_list:
        data = BeautifulSoup(str(product), 'lxml')
        #print(data)
        product_data = data.find('a', {'class': 'js-product-name'})
        #print(product_data)
        name = cleanText(product_data['title'])
        #print(name)
        ratio = fuzz.ratio(product_code.lower(), name.lower())
        print(ratio)
        if ratio > 50:
            link = "https://mediamarkt.pl" + product_data['href']
            #print(link)
            price = cleanPrice(product_data['data-offer-price'])
            #print(price)
            data_set = {'item': name, 'price': price, 'link': link}
            return_dict['mediamarkt'] = data_set
            return
        else:
            continue
    return_dict['mediamarkt'] = None