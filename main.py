import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

def amazonSearch(search_query):
    amazonSearchURL = 'https://www.amazon.com/s?k={0}'.format(search_query)
    
    response = requests.get(amazonSearchURL + '&page=0', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    firstProductDiv = soup.find_all('div', {'data-index': '2'})
    productName = firstProductDiv[0].find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).getText()
    productPrice = (float)(firstProductDiv[0].find('span', {'class': 'a-offscreen'}).getText()[1:])
    productLink = 'https://www.amazon.com' + str(firstProductDiv[0].find('a', {'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']).replace('amp;','')
    
    return productName, productPrice, productLink

def kohlsSearch(search_query):
    kohlsSearchURL = 'https://www.kohls.com/search.jsp?submit-search=web-regular&search={0}'.format(search_query)
    
    response = requests.get(kohlsSearchURL + '&page=0', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    productPrice = (float)(soup.find('span', {'class': 'prod_price_amount red_color'}).getText()[1:])
    productNameDiv = soup.find('div',{'class':'prod_nameBlock'})
    productName = productNameDiv.getText().replace('\n', '').strip()
    productLink = 'https://www.kohls.com/' + productNameDiv.find('p')['rel']

    return productName, productPrice, productLink

def walmartSearch(search_query):
    walmartSearchURL = 'https://www.walmart.com/search?q={0}'.format(search_query)
    
    response = requests.get(walmartSearchURL + '&page=1', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    firstProductDiv = soup.find_all('div', {'class':'mb1 ph1 pa0-xl bb b--near-white w-25'})
    productName = firstProductDiv[0].find('span',{'class':'w_Bl'}).getText()
    productPrice = (float)(firstProductDiv[0].find('div',{'data-automation-id':'product-price'}).find('span',{'class':'w_Bl'}).getText()[15:])
    productLink = firstProductDiv[0].find('a')['href']

    return productName, productPrice, productLink