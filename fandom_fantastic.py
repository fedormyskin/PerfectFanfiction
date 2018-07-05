# -*- coding: utf-8 -*-
"""
Perform Stats on AO3 -- What are the most popular fandoms
Date accessed 3/11/2017
"""
#%% Imports
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import re


#%% Grab the URL


url = 'http://archiveofourown.org/media'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

#%% Get data into table

uggo_fandom = soup.find('ul', attrs={'class':'media fandom index group'}).contents
df = pd.DataFrame(columns= ['Fandom','Works','Category'])
for each in uggo_fandom:
    #grab headings -- COMPLETE    
    heading = each.find('h3')
    if heading !=-1:
        heading = heading.find('a').contents
        #print(heading)
    ol = each.find('ol')
    #print(ol)
    if ol != -1:
        
        for li in ol.find_all('li'):
            if li !=-1:
                fandom = zip(('Fandom', 'Works'),li.stripped_strings)
                fandom.append(('Category', heading[0]))
                newdict = dict(fandom)
                keys = newdict.keys()
                #print(newdict)
                df = df.append(newdict, ignore_index = True)
                #df.append(df2, ignore_index = True)

df = df[df.Category != 'Uncategorized Fandoms']
work_counts_str = df.Works

for i, each in enumerate(work_counts_str):
    str1 = each.split('(')[1]
    str2 = str1.split(')')[0]
    count = int(str2)
    df.set_value(i, 'Works', count)
    
    
df.head()

    
#%%    plot the data
    
    df.sort(['Works'], ascending = False)

