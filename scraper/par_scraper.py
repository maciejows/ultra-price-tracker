import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
from scraper import webdrvr as wd
import lxml

# BeautifulSoup - for parsing HTML.


header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

# header-HTTP headers provide additional parameters to HTTP transactions.
# By sending the appropriate HTTP headers, one can access the response data in a different format.
def cleanText(text):
    return text.strip().replace('\n', '').replace('\t', '').replace(
            '  ', '').replace("\xa0", "")

def clean_price(text):
    return text.replace('\n', '').replace('\t', '').replace(
        ' ', '').replace("\xa0", "").replace("zł", "").replace("zl", "").replace(",", ".")

def fix_url(url):
    if url is None or url == 404:
        return None
    url = str(url)
    if url.startswith("www"):
        return "http://"+url
    else:
        return url

def euro(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['euro'] = None
        return
    result = requests.get(base_url, headers=header)
    # result - this is the response object returned by the get method.
    # Here, we pass the base_url and header as parameters.
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = float(clean_price(soup.find("div", {'class': 'price-normal selenium-price-normal'}).text))
        name = cleanText(soup.find("h1", {'class': 'selenium-KP-product-name'}).text)
        link = base_url
        img = soup.find("a", {'id': 'big-photo'}).attrs['href']
        data_set = {'item': name, 'price': price, 'link': link, 'img': img}
        return_dict['euro'] = data_set
        return
    else:
        print(result.status_code)
        return_dict['euro'] = None

def mediaexpert(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['mediaexpert'] = None
        return
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = float(clean_price(soup.find("span", {'class': 'a-price_price'}).text))
        name = cleanText(soup.find("h1", {'class': 'a-typo is-primary'}).text)
        link = base_url
        img = 'https://www.mediaexpert.pl' + soup.find("div", {'class': 'c-offerBox_galleryItem'}).contents[0]['data-src']
        data_set = {'item': name, 'price': price, 'link': link, 'img': img}
        return_dict['mediaexpert'] = data_set
        return
    else:
        print(result.status_code)
        return_dict['mediaexpert'] = None

def mediamarkt(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['mediamarkt'] = None
        return
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = float(clean_price(soup.find("span", {'itemprop': 'price'}).text))
        name = cleanText(soup.find("h1", {'class': 'm-typo m-typo_primary'}).text)
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return_dict['mediamarkt'] = data_set
        return
    else:
        print(result.status_code)
        return_dict['mediamarkt'] = None


def xkom(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['xkom'] = None
        return
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = float(clean_price(soup.find("meta", {'property': 'product:price:amount'})['content']))
        name = cleanText(soup.find("div", {'class': 'col-xs-12 product-detail-impression'})['data-product-name'])
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return_dict['xkom'] = data_set
    else:
        return_dict['xkom'] = None
        print(result.status_code)

def neo24(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['neo24'] = None
        return
    page = wd.get_page_neo24(base_url)
    soup = BeautifulSoup(page, 'html.parser')
    # file = open("result.html", 'w')
    # file.write(page)
    # file.close()
    try:
        name = cleanText(soup.select('h1[class*="productFullDetailDesktopCss-neo24-productName"]')[0].contents[0].string)
        decimal = "0." + soup.select('div[class*="productShopCss-neo24-sp__fraction"]')[0].contents[0]
        price = float(clean_price(soup.select('div[class*="productShopCss-neo24-sp__root"]')[0].contents[0].string)) + float(decimal)
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return_dict['neo24'] = data_set
        return
    except:
        return_dict['neo24'] = None

def morele(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['morele'] = None
        return
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = float(clean_price(soup.find("div", {'id': 'product_price_brutto'}).text))
        name = cleanText(soup.find("h1", {'class': 'prod-name'}).text)
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return_dict['morele'] = data_set
        return
    else:
        return_dict['morele'] = None
        print(result.status_code)

def komputronik(base_url, return_dict):
    base_url = fix_url(base_url)
    if base_url is None:
        return_dict['komputronik'] = None
        return
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        price = clean_price((soup.find("span", {'class': 'price'})).contents[1].text)
        name = soup.find("title").text
        name = cleanText(name[0:name.find("|")].strip())
        link = base_url
        data_set = {'item': name, 'price': price, 'link': link}
        return_dict['komputronik'] = data_set
        return
    else:
        return_dict['komputronik'] = None
        print(result.status_code)
