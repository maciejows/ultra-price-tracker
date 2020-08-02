import ast

import requests
# requests - will be used to make Http requests to the webpage.
import json
# json - we'll use this to store the extracted information to a JSON file.
from bs4 import BeautifulSoup
import re

from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import multiprocessing
from scraper.scrpr import UpcScrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
import queue
import threading
import time

options = Options()
options.add_argument('--headless')



if __name__ == '__main__':
   ratio = fuzz.ratio('Apple iPhone 11 Pro 64GB (srebrny)'.lower(), 'Smartfon Samsung 11 Pro 64GB MWC32PM/A'.lower())
   print(ratio)