import multiprocessing
import scraper.parser as sp
from scraper.scrpr import UpcScrapper
import scraper.webdrvr as wd
import scraper.par_scraper as ps
from fuzzywuzzy import fuzz

# gets url as parameter
def get_all_data_url(url):
    data = get_data_from_url(url)
    pages = get_pages(data['item'])
    return scrap_all_phrase(data['item'], pages)

# gets phrase that user entered as parameter
def get_all_data_phrase(phrase):
    pages = get_pages(phrase)
    return scrap_all_phrase(phrase, pages)

# gets URL of the stores as parameter with following pattern
# {'store_name': 'product_url', 'store_name2': 'product_url2', etc.}
def get_new_prices(url_array):
    manager = multiprocessing.Manager()
    new_data = manager.dict()
    euro = multiprocessing.Process(target=ps.euro, args=(url_array['euro'], new_data))
    euro.start()
    mediaexpert = multiprocessing.Process(target=ps.mediaexpert, args=(url_array['mediaexpert'], new_data))
    mediaexpert.start()
    '''
    mediamarkt = multiprocessing.Process(target=ps.mediamarkt, args=(url_array['mediamarkt'], new_data))
    mediamarkt.start()
   neo24 = multiprocessing.Process(target=ps.neo24, args=(url_array['neo24'], new_data))
    neo24.start()'''
    morele = multiprocessing.Process(target=ps.morele, args=(url_array['morele'], new_data))
    morele.start()
    komputronik = multiprocessing.Process(target=ps.komputronik, args=(url_array['komputronik'], new_data))
    komputronik.start()
    euro.join()
    mediaexpert.join()
    '''mediamarkt.join()
    neo24.join()'''
    morele.join()
    komputronik.join()
    '''new_data = {}
    new_data['euro'] = scraper.euro(url_array['euro'])
    new_data['mediaexpert'] = scraper.mediaexpert(url_array['mediaexpert'])
    new_data['morele'] = scraper.morele(url_array['morele'])
    new_data['neo24'] = scraper.neo24(url_array['neo24'])
    new_data['komputronik'] = scraper.komputronik(url_array['komputronik'])
    new_data['mediamarkt'] = scraper.mediamarkt(url_array['mediamarkt'])'''
    return new_data

# gets data regarding stores as parameter with following pattern
# {'store_name': None, 'store_name2': {product_data},'store_name3': {data},'store_name4': None, etc.}
# if the value is None then it checks if the product is now available
def get_missing_data(product):
    collection = scrap_all_phrase(product, get_pages(product))
    return collection


def best_matching_result(phrase, data_dict):
    shopdata = ['morele', 'mediaexpert', 'euro']
    best_match = {'ratio': 0, 'data': {}}
    for shop in shopdata:
        if fuzz.ratio(phrase, data_dict[shop]['item']) > best_match['ratio']:
            best_match['ratio'] = fuzz.ratio(phrase, data_dict[shop]['item'])
            best_match['data'] = data_dict[shop]
    return best_match['data']['item']

def get_data_from_url(url):
    scrap = UpcScrapper()
    if 'euro.com.pl' in url:
        return scrap.euro(url)
    if 'morele.net' in url:
        return scrap.morele(url)
    if 'x-kom.pl' in url:
        return scrap.xkom(url)
    if 'mediaexpert.pl' in url:
        return scrap.mediaexpert(url)
    if 'mediamarkt.pl' in url:
        return scrap.mediamarkt(url)
    if 'komputronik.pl' in url:
        return scrap.komputronik(url)
    if 'neo24.pl' in url:
        return scrap.neo24(url)

# gets name of the product as parameter
def get_pages(name):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    try:
        euro = multiprocessing.Process(target=wd.search_euro, args=(name, data_dict))
        euro.start()
        mediaexpert = multiprocessing.Process(target=wd.search_mediaexpert, args=(name, data_dict))
        mediaexpert.start()
        '''mediamarkt = multiprocessing.Process(target=wd.search_mediamarkt, args=(name, data_dict))
        mediamarkt.start()
        neo24 = multiprocessing.Process(target=wd.search_neo24, args=(name, data_dict))
        neo24.start()'''
        morele = multiprocessing.Process(target=wd.search_morele, args=(name, data_dict))
        morele.start()
        komputronik = multiprocessing.Process(target=wd.search_komputronik, args=(name, data_dict))
        komputronik.start()

        euro.join()
        mediaexpert.join()
        '''mediamarkt.join()
        neo24.join()'''
        morele.join()
        komputronik.join()
        print("all data covered")
        pages = data_dict
    except:
        print("Error getting pages. Please retry.")
        return None
    return pages

# gets searched phrase and pages source code
def scrap_all_phrase(phrase, pages):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    euro = multiprocessing.Process(target=sp.euro, args=(str(pages['euro']), phrase, data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=sp.mediaexpert,
                                          args=(str(pages['mediaexpert']), phrase, data_dict))
    mediaexpert.start()
    #mediamarkt = multiprocessing.Process(target=sp.mediamarkt, args=(str(pages['mediamarkt']), phrase, data_dict))
    #mediamarkt.start()
    #neo24 = multiprocessing.Process(target=sp.neo24, args=(str(pages['neo24']), phrase, data_dict))
    #neo24.start()
    morele = multiprocessing.Process(target=sp.morele, args=(str(pages['morele']), phrase, data_dict))
    morele.start()
    komputronik = multiprocessing.Process(target=sp.komputronik,
                                          args=(str(pages['komputronik']), phrase, data_dict))
    komputronik.start()
    komputronik.join()
    morele.join()
    mediaexpert.join()
    euro.join()
    return data_dict


def find_phrase_in_three_stores(phrase):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    euro = multiprocessing.Process(target=wd.search_euro, args=(phrase, data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=wd.search_mediaexpert, args=(phrase, data_dict))
    mediaexpert.start()
    morele = multiprocessing.Process(target=wd.search_morele, args=(phrase, data_dict))
    morele.start()

    morele.join()
    mediaexpert.join()
    euro.join()
    return data_dict


def get_product_data_phrase(phrase):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    pages = find_phrase_in_three_stores(phrase)
    euro = multiprocessing.Process(target=sp.euro_top, args=(str(pages['euro']), phrase, data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=sp.mediaexpert_top, args=(str(pages['mediaexpert']), phrase, data_dict))
    mediaexpert.start()
    morele = multiprocessing.Process(target=sp.morele_top, args=(str(pages['morele']), phrase, data_dict))
    morele.start()
    morele.join()

    mediaexpert.join()
    euro.join()
    '''--------------------------------------------------------'''
    searching_phrase = best_matching_result(phrase, data_dict)
    data_dict.clear()
    return get_all_data_phrase(searching_phrase)
