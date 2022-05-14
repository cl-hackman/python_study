from bs4 import BeautifulSoup as bs

import requests

'''Remember to learn debuggin for this'''
try:
    req = requests.get('https://www.bloomingdales.com/shop/search?keyword=karl%20lagerfeld%20paris%20in%20Men#4194383').text
    soup = bs(req, 'lxml')
    parent = soup.find('ul', class_ ='items grid-x grid-padding-x').find_all('li', class_ ='small-6 medium-4 large-4 cell').text
    for x in parent:
        description = x.find('div', class_ ='productDescription').text
        price = x.find('div', class_ ='productDetail')
        links = x.find('div', class_ ="productThumbnail selectedProductThumbnail").a.text
        print(f"Description: {description}")
        print(f"Price: {price}")
        print(f"Link: {links}")
except:
    pass



