import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

def neo24Scraper(base_url):
    result = requests.get(base_url, headers=header)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        print(soup.body)
        print(soup.find('div', {'class': "productShopCss-neo24-product__price-12m"}))
        #print(soup.select("div[class*='productShopCss-neo24-product__price']")[0].contents[0].contents[0])
        #return float(soup.select("div[class*='productShopCss-neo24-product__price']")[0].contents[0].contents[0].strip())
    else:
        return result.status_code

if __name__ == "__main__":
    #entered_expression = 'Telewizor PHILIPS 55" 55PUS6704 UHD'
    #page = open('neo24List.html', encoding='utf-8')
    print(neo24Scraper("https://www.neo24.pl/philips-55-55pus6704-uhd.html"))