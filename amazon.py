# scrap multiple pages on a website


from requests_html import HTMLSession
from bs4 import BeautifulSoup
s = HTMLSession()

url = 'https://www.mi.com/global/product-list'
       

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def getnextpage(soup):
    page = soup.find('ul', {'class': 'mi-pagination product-catalogue__pager'})
    if not page.find('li', {'class': 'mi-pagination-item mi-pagination-item-13 mi-pagination-item-active'}):
        url =  'http://amazon.co.uk' + str(page.find('li', {'class': 'a-list'}).find('a')['href'])
        return url
    else:
        return
    

while True:
    soup = getdata(url)
    url = getnextpage(soup)
    if not url:
        break
    print(url)


