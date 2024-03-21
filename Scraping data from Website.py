#!/usr/bin/env python
# coding: utf-8

# # Find and Find all

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url='https://www.scrapethissite.com/pages/forms/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())


# In[18]:


soup.find('p',class_='lead').text.strip()


# In[29]:


soup.find('th').text.strip()


# # Scraping data from a Real Website + panda

# In[93]:


from bs4 import BeautifulSoup
import requests


# In[94]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue#:~:text=Walmart%20has%20been%20the%20world%27s%20largest%20company%20by,the%20world%27s%20largest%20company%20by%20revenue%20since%202014.'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')


# In[95]:


table=soup.find_all('table')[0]
print(table)


# In[96]:


world_titles=table.find_all('th')
print(world_titles)


# In[100]:


world=[title.text.strip() for title in world_titles]

print(world)


# In[103]:


import pandas as pd


# In[133]:


df=pd.DataFrame(columns=world)
df


# In[139]:


#it will have all the data of table rows
column_data=table.find_all('tr')
column_data=column_data[2:]
df


# In[145]:


#parsing the table row data
for row in column_data:
    #here we will try to find the data of the individual rows
    row_data=row.find_all('td')
    #Cleaning the raw data to find the required text
    world_data=[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length]=world_data


# In[148]:


df.to_csv(r'C:\Users\devma\OneDrive\Desktop\Python_Tutorial\Companies.csv')

