import requests #requests - will be used to make Http requests to the webpage.
import json #json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup #BeautifulSoup - for parsing HTML.

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
#header-HTTP headers provide additional parameters to HTTP transactions. By sending the appropriate HTTP headers, one can access the response data in a different format.
base_url = "https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-55ep640-tv-led-4k-android.bhtml"
#base_url - is the webpage we want to scrape since we'll be needing the URL quite often, it's good to have a single initialization and reuse this variable going forward.
r = requests.get(base_url, headers=header)
#r - this is the response object returned by the get method. Here, we pass the base_url and header as parameters.
if r.status_code == 200:
  soup = BeautifulSoup(r.text, 'html.parser')
  print(soup.find("div", {'class':'price-normal selenium-price-normal'}).text)

  
else:
  print(r.status_code)
  #"#product-top > div.product-sales.product-sales-50461416929 > div.product-categories.product-categories-50461416929 > div > div.product-price.price-show.instalments-show.has-leasing-offer > div.price-voucher > div.price-normal.selenium-price-normal")