# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import Fandom2 as fd
import pandas as pd
import numpy as np
from time import time

#get the urls for each type

fandomtypes = fd.get_fandoms_from_page()
allfandoms = []
for eachfandom in fandomtypes:
        thistypes = fd.get_list_from_fandom_page(eachfandom)
        allfandoms.extend(thistypes)

fandomstouse = list(set(allfandoms))
print(time())
works = pd.DataFrame()
for fandom in fandomstouse:
        [df1, soupy] = fd.get_works_from_page(fandom) 
        works.append(df1, ignore_index = True)
        
        
        
        
        
        
        
        print(time())

#works.drop_duplicates(inplace = True)



#for each in urls:
#        r = requests.get(each)
#        soup = BeautifulSoup(r.content, 'lxml')
#        
#        
#        header = soup.find('ol', attrs={'class':'pagination actions'})
#        
#        if header:
#                #get the url of the next page
#                nextbutton = header.find('li', attrs={"class":"next"})
#                a = nextbutton.find('a')
#                if a:
#                        nexturl = a['href']
#                        print(nexturl)
#        else: #if there are less than twenty works
#                