#https://stackoverflow.com/questions/36730372/extract-the-text-from-p-within-div-with-beautifulsoup
    
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def bing_search(query):
    url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
    custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    req = Request(url, headers={"User-Agent": custom_user_agent})
    page = urlopen(req)
    soup = BeautifulSoup(page.read(),"lxml")
    snippet = soup.find_all("li", { "class" : "b_algo" }) # estructura principal de resultados
    docs = [x.find('p').text for x in snippet if x.find('p') is not None] # generalmente el snippet esta contenido en un p
    return docs[:3]