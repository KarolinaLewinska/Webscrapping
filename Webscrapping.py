#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
import re 
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# In[3]:


#avans.pl
#laptops

pages_url = []
pages_url.append('')
for page_url in range (2, 42):
    pages_url.append('?page=' + str(page_url))

#names and prices
file = open('avans_laptops.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price' + '\n')

for page_url in pages_url:
    avans_url = requests.get('https://www.avans.pl/komputery-i-tablety/laptopy-i-ultrabooki/laptopy' + page_url)
    data = BeautifulSoup(avans_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'a-typo is-secondary'})
    prices_int = data.findAll('span', attrs = {'class': 'a-price_price'})
    prices_decimal = data.findAll('span', attrs = {'class': 'a-price_meta'})
    joined_prices = []
    
    for i in range(len(prices_int)):
        price_no_currency = prices_decimal[i].text.strip().replace('zł', '')
        joined_prices.append(prices_int[i].text.strip() + price_no_currency.replace(',', '.'))
    
    prices = []       
    for i in range(len(joined_prices)):
        if float(joined_prices[i]) >= 999:
            prices.append(joined_prices[i])
        
    for name, price in zip(names, prices):   
        file.write(name.text.strip() + ';' + price + '\n')
file.close()


# In[4]:


#phones

pages_url = []
pages_url.append('')
for page_url in range (2, 44):
    pages_url.append('?page=' + str(page_url))

#names and prices
file = open('avans_phones.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price' + '\n')

for page_url in pages_url:
    avans_url = requests.get('https://www.avans.pl/telefony-i-smartfony/smartfony' + page_url)
    data = BeautifulSoup(avans_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'a-typo is-secondary'})
    prices_int = data.findAll('span', attrs = {'class': 'a-price_price'})
    prices_decimal = data.findAll('span', attrs = {'class': 'a-price_meta'})
    joined_prices = []
    
    for i in range(len(prices_int)):
        price_no_currency = prices_decimal[i].text.strip().replace('zł', '')
        joined_prices.append(prices_int[i].text.strip() + price_no_currency.replace(',', '.'))
    
  
    prices = []       
    for i in range(len(joined_prices)):
        if float(joined_prices[i]) >= 43:
            prices.append(joined_prices[i])
        
    for name, price in zip(names, prices):   
        file.write(name.text.strip() + ';' + price +'\n')
file.close()


# In[5]:


#morele.net
#laptops

pages_url = []
pages_url.append('')
for page_url in range (2, 51):
    pages_url.append(',,,,,,,,0,,,,/' + str(page_url) + '/')

#names and prices
file = open('morele_laptops.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price' + '\n')

for page_url in pages_url:
    morele_url = requests.get('https://www.morele.net/kategoria/laptopy-31/' + page_url)
    data = BeautifulSoup(morele_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'productLink'})
    prices = data.findAll('div', attrs = {'class': 'price-new'})
    for name, price in zip(names, prices):
        price_no_currency = price.text.strip().replace('zł', '')
        price_no_comma = price_no_currency.replace(',', '.')
        price = re.sub('\s', '', price_no_comma)
        file.write(name.text.strip() + ';' + price +'\n')
file.close()


# In[6]:


#phones

pages_url = []
pages_url.append('')
for page_url in range (2, 43):
    pages_url.append(',,,,,,,,0,,,,/' + str(page_url) + '/')

#names and prices
file = open('morele_phones.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price ( in zl)' + '\n')

for page_url in pages_url:
    morele_url = requests.get('https://www.morele.net/kategoria/smartfony-280/' + page_url)
    data = BeautifulSoup(morele_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'productLink'})
    prices = data.findAll('div', attrs = {'class': 'price-new'})
    for name, price in zip(names, prices):
        price_no_currency = price.text.strip().replace('zł', '')
        price_no_comma = price_no_currency.replace(',', '.')
        price = re.sub('\s', '', price_no_comma)
        file.write(name.text.strip() + ';' + price + '\n')
file.close()


# In[7]:


#vobis
#laptops

pages_url = []
pages_url.append('')
for page_url in range (2, 176):
    pages_url.append('?page=' + str(page_url))

#names and prices
file = open('vobis_laptops.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price' + '\n')

for page_url in pages_url:
    vobis_url = requests.get('https://vobis.pl/komputery/laptopy' + page_url)
    data = BeautifulSoup(vobis_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'js-analyticsLink js-analyticsData'})
    prices = data.findAll('p', attrs = {'class': 'm-offerBox_price'})
    for name, price in zip(names, prices):
        price_no_currency = price.text.strip().replace('zł', '')
        price_no_comma = price_no_currency.replace(',', '.')
        price = re.sub('\s', '', price_no_comma)
        file.write(name.text.strip() + ';' + price +'\n')
file.close()


# In[8]:


#phones

pages_url = []
pages_url.append('')
for page_url in range (2, 25):
    pages_url.append('?page=' + str(page_url))

#names and prices
file = open('vobis_phones.csv', 'w', encoding = 'utf-8')
file.write('name' + ';' + 'price' + '\n')

for page_url in pages_url:
    vobis_url = requests.get('https://vobis.pl/smartfony-i-telefony/smartfony' + page_url)
    data = BeautifulSoup(vobis_url.text, 'html.parser')
    names = data.findAll('a', attrs = {'class': 'js-analyticsLink js-analyticsData'})
    prices = data.findAll('p', attrs = {'class': 'm-offerBox_price'})
    for name, price in zip(names, prices):
        price_no_currency = price.text.strip().replace('zł', '')
        price_no_comma = price_no_currency.replace(',', '.')
        price = re.sub('\s', '', price_no_comma)
        file.write(name.text.strip() + ';' + price + '\n')
file.close()


# In[9]:


avans_laptops = pd.read_csv('data/avans_laptops.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')
avans_phones = pd.read_csv('data/avans_phones.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')

morele_laptops = pd.read_csv('data/morele_laptops.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')
morele_phones = pd.read_csv('data/morele_phones.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')

vobis_laptops = pd.read_csv('data/vobis_laptops.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')
vobis_phones = pd.read_csv('data/vobis_phones.csv', sep = ';', decimal = '.', encoding = 'unicode_escape')


# In[10]:


def search_by_price_range(min_value, max_value, file):
    results = file.loc[(file.price >= min_value) & (file.price <= max_value)].sort_values(['price'], ascending = 1)
    results_occurence = results.count()
    mean_value = results.mean()
    min_value = min(results.price, default='EMPTY')
    max_value = max(results.price, default='EMPTY')
    display('Minimal price ' + str(min_value))
    display('Maximal price ' + str(max_value))
    display('Average ' + str(mean_value))
    display('Number of results')
    display(results_occurence)
    display(results)


# In[11]:


def search_by_keyword(keyword, file):
    results = file.loc[(file['name'].str.contains(keyword))].sort_values(['price'], ascending = 1)
    results_occurence = results.count()
    mean_value = results.mean()
    min_value = min(results.price, default='EMPTY')
    max_value = max(results.price, default='EMPTY')
    display('Minimal price ' + str(min_value))
    display('Maximal price ' + str(max_value))
    display('Average ' + str(mean_value))
    display('Number of results')
    display(results_occurence)
    display(results)


# In[12]:


def search_the_highest_prices(number_of_prices, file):
    results = file.nlargest(number_of_prices, ['price']).sort_values(['price'], ascending = 0)
    mean_value = results.mean()
    min_value = min(results.price, default='EMPTY')
    max_value = max(results.price, default='EMPTY')
    display('Minimal price ' + str(min_value))
    display('Maximal price ' + str(max_value))
    display('Average ' + str(mean_value))
    display(results)


# In[13]:


def search_the_lowest_prices(number_of_prices, file):
    results = file.nsmallest(number_of_prices, ['price']).sort_values(['price'], ascending = 1)
    mean_value = results.mean()
    min_value = min(results.price, default='EMPTY')
    max_value = max(results.price, default='EMPTY')
    display('Minimal price ' + str(min_value))
    display('Maximal price ' + str(max_value))
    display('Average ' + str(mean_value))
    display(results)


# In[14]:


display(avans_laptops)


# In[15]:


avans_laptops.info()
print('\n')
morele_laptops.info()
print('\n')
vobis_laptops.info()


# In[16]:


avans_phones.info()
print('\n')
morele_phones.info()
print('\n')
vobis_phones.info()


# In[17]:


avans_laptops.price.describe() 


# In[18]:


morele_laptops.price.describe()


# In[19]:


vobis_laptops.price.describe() 


# In[20]:


avans_phones.price.describe() 


# In[21]:


morele_phones.price.describe()


# In[22]:


vobis_phones.price.describe() 


# In[23]:


search_by_price_range(1, 3500, avans_laptops)


# In[24]:


search_by_price_range(1, 3500, morele_laptops)


# In[25]:


search_by_price_range(1, 3500, vobis_laptops)


# In[26]:


search_by_price_range(1, 2000, avans_phones)


# In[27]:


search_by_price_range(1, 2000, morele_phones)


# In[28]:


search_by_price_range(1, 2000, vobis_phones)


# In[29]:


search_the_highest_prices(10, avans_laptops)


# In[30]:


search_the_highest_prices(10, morele_laptops)


# In[31]:


search_the_highest_prices(10, vobis_laptops)


# In[32]:


search_the_lowest_prices(10, avans_laptops)


# In[33]:


search_the_lowest_prices(10, morele_laptops)


# In[34]:


search_the_lowest_prices(10, vobis_laptops)


# In[35]:


search_the_highest_prices(10, avans_phones)


# In[36]:


search_the_highest_prices(10, morele_phones)


# In[37]:


search_the_highest_prices(10, vobis_phones)


# In[38]:


search_the_lowest_prices(10, avans_phones)


# In[39]:


search_the_lowest_prices(10, morele_phones)


# In[40]:


search_the_lowest_prices(10, vobis_phones)


# In[41]:


search_by_keyword('LENOVO', avans_laptops)
search_by_keyword('DELL', avans_laptops)
search_by_keyword('HP', avans_laptops)
search_by_keyword('ACER', avans_laptops)
search_by_keyword('ASUS', avans_laptops)
search_by_keyword('HUAWEI', avans_laptops)
search_by_keyword('XIAOMI', avans_laptops)
search_by_keyword('APPLE', avans_laptops)


# In[42]:


search_by_keyword('Lenovo', morele_laptops)
search_by_keyword('Dell', morele_laptops)
search_by_keyword('HP', morele_laptops)
search_by_keyword('Acer', morele_laptops)
search_by_keyword('Asus', morele_laptops)
search_by_keyword('Huawei', morele_laptops)
search_by_keyword('Xiaomi', morele_laptops)
search_by_keyword('Apple', morele_laptops)


# In[43]:


search_by_keyword('Lenovo', vobis_laptops)
search_by_keyword('Dell', vobis_laptops)
search_by_keyword('HP', vobis_laptops)
search_by_keyword('Acer', vobis_laptops)
search_by_keyword('Asus', vobis_laptops)
search_by_keyword('Huawei', vobis_laptops)
search_by_keyword('Xiaomi', vobis_laptops)
search_by_keyword('Apple', vobis_laptops)


# In[44]:


search_by_keyword('SAMSUNG', avans_phones)
search_by_keyword('APPLE', avans_phones)
search_by_keyword('HUAWEI', avans_phones)
search_by_keyword('XIAOMI', avans_phones)
search_by_keyword('MOTOROLA', avans_phones)
search_by_keyword('NOKIA', avans_phones)
search_by_keyword('LG', avans_phones)
search_by_keyword('HTC', avans_phones)


# In[45]:


search_by_keyword('Samsung', morele_phones)
search_by_keyword('Apple', morele_phones)
search_by_keyword('Huawei', morele_phones)
search_by_keyword('Xiaomi', morele_phones)
search_by_keyword('Motorola', morele_phones)
search_by_keyword('Nokia', morele_phones)
search_by_keyword('LG', morele_phones)
search_by_keyword('HTC', morele_phones)


# In[46]:


search_by_keyword('Samsung', vobis_phones)
search_by_keyword('Apple', vobis_phones)
search_by_keyword('Huawei', vobis_phones)
search_by_keyword('Xiaomi', vobis_phones)
search_by_keyword('Motorola', vobis_phones)
search_by_keyword('Nokia', vobis_phones)
search_by_keyword('LG', vobis_phones)
search_by_keyword('HTC', vobis_phones)


# In[47]:


avans_laptops['price'].hist()


# In[48]:


morele_laptops['price'].hist()


# In[49]:


vobis_laptops['price'].hist()


# In[50]:


avans_phones['price'].hist()


# In[51]:


morele_phones['price'].hist()


# In[52]:


vobis_phones['price'].hist()

