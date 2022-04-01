#!/usr/bin/env python
# coding: utf-8

# This notebook belongs to Chung Thế Thọ - 19127562

# In[1]:


import requests
import requests_cache
from bs4 import BeautifulSoup
import time
import json
import re
import pandas as pd # Dùng để đọc và hiển thị file csv/tsv
from datetime import datetime, timedelta # Dùng để xử lý dữ liệu thời gian
# YOUR CODE HERE (OPTION) 
# Nếu cần các thư viện khác thì bạn có thể import ở đây

import urllib.robotparser # Kiểm tra file robot.txt có được phép crawl không


# In[2]:


# Tạo dataframe lưu dữ liệu crawl
attrs = ['#', 'Country,Other', 'Total Cases', 'New Cases', 'Total Deaths',
         'New Deaths', 'Total Recovered', 'New Recovered', 'Active Cases',
         'Serious, Critical', 'Tot Cases/1M pop', 'Deaths/1M pop', 'Total Tests',
         'Tests/1M pop', 'Population', 'Region']
df = pd.DataFrame(columns = attrs)


# In[3]:


# URL
url = 'https://www.worldometers.info/coronavirus/#countries'
    
r = requests.get(url)
html_text = r.text
    
# Parse HTML
tree = BeautifulSoup(html_text, 'html.parser')
        
# Tiến hành trích xuất dữ liệu
# chú thích id:
# main_table_countries_today: hôm nay
# main_table_countries_yesterday: hôm qua
# main_table_countries_yesterday2: hôm kia
table = tree.find('table', id='main_table_countries_yesterday2').find('tbody').find_all('tr')


# In[4]:


for i in range(len(table)):
    row = [value.text.strip() for value in table[i] if value != '\n']
    df.loc[len(df)] = row[:16]


# In[5]:


df.head(10)


# In[6]:


from datetime import datetime, timedelta
day_before_yesterday = datetime.today() - timedelta(days=2)

file_name = f"{day_before_yesterday.year}-{day_before_yesterday.month}-{day_before_yesterday.day}.csv"
file_name


# In[7]:


df.to_csv(file_name, index=False)


# In[8]:


test = pd.read_csv(f"./Worldometer-COVID19/dataset/{file_name}")
test.head(10)

