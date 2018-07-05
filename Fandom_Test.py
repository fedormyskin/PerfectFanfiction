# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:50:05 2018

@author: Lady_Locke@hotmail.com (Lockea Stone)
"""

import requests
import Fandom2 as fd
from bs4 import BeautifulSoup
import pandas as pd

url1 = "https://archiveofourown.org/tags/Final%20Fantasy%20VII/works"
url2 = "https://archiveofourown.org/tags/12%20Beast%20(Manga)/works"

r = requests.get(url2)
soup = BeautifulSoup(r.content, 'lxml')

header = soup.find('ol', attrs={'class':'pagination actions'})
works = pd.DataFrame()
df = fd.get_works_from_page(soup)
works = works.append(df)

#if there is more than one page of works
if header:
        nextbutton = header.find('li', attrs={"class":"next"})
        a = nextbutton.find('a')
        i = 0
        while a: #while there is a link in the next button
                nexturl = fd.aothree + a['href']
                r = requests.get(nexturl)
                soup = BeautifulSoup(r.content, 'lxml')
                                
                #grab the works
                df = fd.get_works_from_page(soup)
                works = works.append(df)
                i +=1
                print(i)
                
                header = soup.find('ol', attrs={'class':'pagination actions'})
                nextbutton = header.find('li', attrs={"class":"next"})
                a = nextbutton.find('a')
