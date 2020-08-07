import multiprocessing
import scraper.parser as sp
from scraper.scrpr import UpcScrapper
import scraper.webdrvr as wd


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


def get_pages(name):
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    euro = multiprocessing.Process(target=wd.search_euro, args=(name, data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=wd.search_mediaexpert, args=(name, data_dict))
    mediaexpert.start()
    mediamarkt = multiprocessing.Process(target=wd.search_mediamarkt, args=(name, data_dict))
    mediamarkt.start()
    neo24 = multiprocessing.Process(target=wd.search_neo24, args=(name, data_dict))
    neo24.start()
    morele = multiprocessing.Process(target=wd.search_morele, args=(name, data_dict))
    morele.start()
    komputronik = multiprocessing.Process(target=wd.search_komputronik, args=(name, data_dict))
    komputronik.start()
    euro.join()
    mediaexpert.join()
    mediamarkt.join()
    neo24.join()
    morele.join()
    komputronik.join()
    print("all data covered")
    pages = data_dict
    return pages


def scrap_all_url(url):
    data = get_data_from_url(url)
    #print(data['item'])
    pages = get_pages(data['item'])
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    #print(str(pages['neo24']))
    #print("starting multithreaded parsing")
    #print(pages)
    euro = multiprocessing.Process(target=sp.euro, args=(str(pages['euro']), data['item'], data_dict))
    euro.start()
    mediaexpert = multiprocessing.Process(target=sp.mediaexpert, args=(str(pages['mediaexpert']), data['item'], data_dict))
    mediaexpert.start()
    mediamarkt = multiprocessing.Process(target=sp.mediamarkt, args=(str(pages['mediamarkt']), data['item'], data_dict))
    mediamarkt.start()
    neo24 = multiprocessing.Process(target=sp.neo24, args=(str(pages['neo24']), data['item'], data_dict))
    neo24.start()
    morele = multiprocessing.Process(target=sp.morele, args=(str(pages['morele']), data['item'], data_dict))
    morele.start()
    komputronik = multiprocessing.Process(target=sp.komputronik, args=(str(pages['komputronik']), data['item'], data_dict))
    komputronik.start()
    euro.join()
    mediaexpert.join()
    mediamarkt.join()
    neo24.join()
    morele.join()
    komputronik.join()
    return data_dict


def scrap_all_phrase(phrase):
    collection = {}
    return collection


def get_product_data_from_phrase(phrase):
    product = {}
    return product


def get_new_prices(url_array):
    new_prices = {}
    return new_prices


def get_missing_data(product, store_array):
    collection = {}
    return collection


if __name__ == "__main__":
    #scrap = UpcScrapper()
    #parser = UpcParser()
    print(scrap_all_url("https://www.euro.com.pl/telefony-komorkowe/apple-iphone-pro-11-64gb-srebrny.bhtml"))
    #print(search_mediamarkt("Smartfon APPLE iPhone 11 Pro Max 64GB Złoty"))
    #print(scrap.morele("https://www.morele.net/sluchawki-steelseries-arctis-1-61427-5938473/"))
    #print(scrap.komputronik("https://www.komputronik.pl/product/688817/huawei-matebook-x-pro-2020-green.html"))
    #print(scrap.neo24Scraper(get_page_neo24('https://www.neo24.pl/philips-55-55pus6704-uhd.html')))
    #print(scrap.euro("https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-50ep640-tv-led-4k-android.bhtml"))
    #print(scrap.mediaexpert("https://www.mediaexpert.pl/telewizory-i-rtv/telewizory/telewizor-tcl-led-50ep680x1"))
    #print(scrap.xkom("https://www.x-kom.pl/p/423390-narzedzie-serwisowe-sieciowe-phanteks-toolkit-zestaw-narzedzi.html"))
    #print(scrap.neo24(get_page_neo24("https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"), "https://www.neo24.pl/delonghi-odkamieniacz-ecodecalk-500ml.html"))
    #print(search_mediamarkt("aoc"))
