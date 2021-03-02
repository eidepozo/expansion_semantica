#https://stackoverflow.com/questions/36730372/extract-the-text-from-p-within-div-with-beautifulsoup
    
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time

def bing_search(query):
    url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
    #custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
    req = Request(url, headers={"User-Agent": custom_user_agent})
    page = urlopen(req)
    soup = BeautifulSoup(page.read(),"lxml")
    snippet = soup.find_all("li", { "class" : "b_algo" }) # estructura principal de resultados
    docs = [x.find('p').text for x in snippet if x.find('p') is not None] # generalmente el snippet esta contenido en un p
    return docs[:3]


def bing_search_alt(query):
    url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
    driver = webdriver.Firefox()
    driver.get(url)
    elements = WebDriverWait(driver,12).until(presence_of_all_elements_located((By.CSS_SELECTOR, 'div.b_caption p')))
    docs = [value.text for value in elements[:3]]
    time.sleep(3)
    driver.close()
    return docs    