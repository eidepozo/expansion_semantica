#https://stackoverflow.com/questions/36730372/extract-the-text-from-p-within-div-with-beautifulsoup
    
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
from selenium.webdriver.support import expected_conditions as EC
from dateutil.parser import parse

import re

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
    elements = WebDriverWait(driver,6).until(presence_of_all_elements_located((By.CSS_SELECTOR, 'li.b_algo p')))
    docs = [value.text for value in elements[:3]]
    while len(docs) != 3:
        next_page=WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b_results > li.b_pag > nav > ul > li:last-child")))
        next_page.click()
        elements = WebDriverWait(driver,6).until(presence_of_all_elements_located((By.CSS_SELECTOR, 'li.b_algo p')))
        for value in elements[:3-len(docs)]:
            docs.append(value.text) 
    time.sleep(3)
    driver.close()
    docs = [re.sub('[·]', '', d) for d in docs]
    try:
        processed_docs = [d.split(' ', 1)[1].strip() if is_date(d.split()[0]) else d for d in docs]
    except IndexError:
        print(docs)
    return processed_docs  

#https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

 