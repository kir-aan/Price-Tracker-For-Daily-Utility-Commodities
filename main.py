import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

search_query = input("Enter search key: ").replace(' ', '+')


#AMAZON
amazonSearchURL = 'https://www.amazon.com/s?k={0}'.format(search_query)

response = requests.get(amazonSearchURL + '&page=0', headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

firstProductDiv = soup.find_all('div', {'data-index': '2'})
print('---------------------------------------')
print('AMAZON')
amzProductName = firstProductDiv[0].find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).getText()
print('Product Name: ',amzProductName)
amzProductPrice = firstProductDiv[0].find('span', {'class': 'a-offscreen'}).getText()
print('Product Price: ', amzProductPrice)
amzProductLink = 'https://www.amazon.com' + str(firstProductDiv[0].find('a', {'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']).replace('amp;','')
print('Product Link: ',amzProductLink)
print('---------------------------------------')
print()

#KOHLS
print('---------------------------------------')
print("KOHLS")
kohlsSearchURL = 'https://www.kohls.com/search.jsp?submit-search=web-regular&search={0}'.format(search_query)
response = requests.get(kohlsSearchURL + '&page=0', headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
productPriceSpan = soup.find('span', {'class': 'prod_price_amount red_color'})
productNameDiv = soup.find('div',{'class':'prod_nameBlock'})
productLinkP = productNameDiv.find('p')['rel']

print('Product Name: ',productNameDiv.getText().replace('\n', '').lstrip())
print('Product Price: ',productPriceSpan.getText())
print('https://www.kohls.com/'+productLinkP)
print('---------------------------------------')
print()

#WALMART
walmartSearchURL = 'https://www.walmart.com/search?q={0}'.format(search_query)
response = requests.get(walmartSearchURL + '&page=1', headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
firstProductDiv = soup.find_all('div', {'class':'mb1 ph1 pa0-xl bb b--near-white w-25'})

print('---------------------------------------')
print('WALMART')
# print('Product Name: ',firstProductSpan[0].getText())
print('Product Name: ',firstProductDiv[0].find('span',{'class':'w_Bl'}).getText())
print('Product Price:', firstProductDiv[0].find('div',{'data-automation-id':'product-price'}).find('span',{'class':'w_Bl'}).getText())
print('Product Link: ', firstProductDiv[0].find('a')['href'])
print('---------------------------------------')
print()