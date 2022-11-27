import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

def extractPrice(productPriceString):
    price = ''
    found = False
    for p in productPriceString:
        if(p == '$'):
            found = True
            continue
        if(found):
            if(p==' '):
                break
            price += p
    return (float)(price)
    

#Peforms search on amazon.com and returns the result
def amazonSearch(search_query):
    amazonSearchURL = 'https://www.amazon.com/s?k={0}'.format(search_query)
    
    response = requests.get(amazonSearchURL + '&page=0', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    firstProductDiv = soup.find('div', {'data-index': '2'})
    productName = firstProductDiv.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).getText()
    productPrice = extractPrice(firstProductDiv.find('span', {'class': 'a-offscreen'}).getText())
    productLink = 'https://www.amazon.com' + str(firstProductDiv.find('a', {'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']).replace('amp;','')
    
    return productName, productPrice, productLink

#Performs search on kohls.com and returns the result
def kohlsSearch(search_query):
    kohlsSearchURL = 'https://www.kohls.com/search.jsp?submit-search=web-regular&search={0}'.format(search_query)
    
    response = requests.get(kohlsSearchURL + '&page=0', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    productPrice = extractPrice(soup.find('span', {'class': 'prod_price_amount red_color'}).getText())
    productNameDiv = soup.find('div',{'class':'prod_nameBlock'})
    productName = productNameDiv.getText().replace('\n', '').strip()
    productLink = 'https://www.kohls.com/' + productNameDiv.find('p')['rel']

    return productName, productPrice, productLink

#Performs search on walmart.com and returns the result
def walmartSearch(search_query):
    walmartSearchURL = 'https://www.walmart.com/search?q={0}'.format(search_query)
    
    response = requests.get(walmartSearchURL + '&page=1', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    firstProductDiv = soup.find('div', {'class':'mb1 ph1 pa0-xl bb b--near-white w-25'})
    productName = firstProductDiv.find('span',{'class':'w_Bl'}).getText()
    productPrice = extractPrice(firstProductDiv.find('div',{'data-automation-id':'product-price'}).find('span',{'class':'w_Bl'}).getText())
    productLink = firstProductDiv.find('a')['href']

    return productName, productPrice, productLink