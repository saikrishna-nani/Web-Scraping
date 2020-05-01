#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import requests and BeautifulSoup libraries
#requests for making http calls
#bs4 for parsing into html tags
import requests as req
from bs4 import BeautifulSoup as bs

#URL to scrape
URL = "https://www.amazon.com/s?k=laptops&page=2&qid=1567174464&ref=sr_pg_2"

#Adding headers to makesure that server treats program as UserAgent
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
           "Accept-Encoding":"gzip, deflate", 
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
           "DNT":"1","Connection":"close", 
           "Upgrade-Insecure-Requests":"1"}

#send Get Request
rawContent = req.get(URL,headers=headers)

#extract and make Content-Type to html5
soup = bs(rawContent.content, 'html5lib')

#find all the tags with attribute 'data-component-type' with value 's-search-result'
soup = soup.findAll('div', attrs = {'data-component-type':'s-search-result'})
productNames =[]

for searchResult in soup:
    #extract each product name tag
    productNames.append(searchResult.find('span',attrs={'class':'a-size-medium'}))
with open('amazon_scrape.txt', 'a') as f: 
    for product in productNames:
        #extract text from product tags
        f.write(product.text+'\n')


# In[ ]:




