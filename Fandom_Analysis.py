# -*- coding: utf-8 -*-
"""
created on tue mar 14 08:17:18 2017

analyze the data aquired from ao3. requires fandoms library

@author: spaceyjo
"""
#%% import libraries

import pandas as pd
import Fandom2 as fd

#%% grab the uls of the top 1-100 fics by hits for marvel

#marvel
#url = ['https://archiveofourown.org/works?utf8=%e2%9c%93&commit=sort+and+filter&work_search%5bsort_column%5d=hits&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5blanguage_id%5d=&work_search%5bcomplete%5d=0&tag_id=marvel',
#'https://archiveofourown.org/tags/marvel/works?commit=sort+and+filter&page=2&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits',
#'https://archiveofourown.org/tags/marvel/works?commit=sort+and+filter&page=3&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits',
#'https://archiveofourown.org/tags/marvel/works?commit=sort+and+filter&page=4&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits',
#'https://archiveofourown.org/tags/marvel/works?commit=sort+and+filter&page=5&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits']

#alternate universe
#url = ['http://archiveofourown.org/works?utf8=%e2%9c%93&commit=sort+and+filter&work_search%5bsort_column%5d=hits&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5blanguage_id%5d=&work_search%5bcomplete%5d=0&tag_id=alternate+universe',
#       'http://archiveofourown.org/tags/alternate%20universe/works?commit=sort+and+filter&page=2&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits'
#       'http://archiveofourown.org/tags/alternate%20universe/works?commit=sort+and+filter&page=3&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits'
#       'http://archiveofourown.org/tags/alternate%20universe/works?commit=sort+and+filter&page=4&utf8=%e2%9c%93&work_search%5bcomplete%5d=0&work_search%5blanguage_id%5d=&work_search%5bother_tag_names%5d=&work_search%5bquery%5d=&work_search%5bsort_column%5d=hits'
#       'http://archiveofourown.org/tags/Alternate%20Universe/works?commit=Sort+and+Filter&page=5&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits']

#teen wolf
#url = ['http://archiveofourown.org/works?utf8=%E2%9C%93&commit=Sort+and+Filter&work_search%5Bsort_column%5D=hits&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&work_search%5Bcomplete%5D=0&tag_id=Teen+Wolf+%28TV%29',
#       'http://archiveofourown.org/tags/Teen%20Wolf%20(TV)/works?commit=Sort+and+Filter&page=2&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Teen%20Wolf%20(TV)/works?commit=Sort+and+Filter&page=3&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Teen%20Wolf%20(TV)/works?commit=Sort+and+Filter&page=4&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Teen%20Wolf%20(TV)/works?commit=Sort+and+Filter&page=5&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits']

#supernatural
#url = ['http://archiveofourown.org/works?utf8=%E2%9C%93&commit=Sort+and+Filter&work_search%5Bsort_column%5D=hits&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&work_search%5Bcomplete%5D=0&tag_id=Supernatural',
#       'http://archiveofourown.org/tags/Supernatural/works?commit=Sort+and+Filter&page=2&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Supernatural/works?commit=Sort+and+Filter&page=3&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Supernatural/works?commit=Sort+and+Filter&page=4&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Supernatural/works?commit=Sort+and+Filter&page=5&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits']

#sherlock
#url = ['http://archiveofourown.org/works?utf8=%E2%9C%93&commit=Sort+and+Filter&work_search%5Bsort_column%5D=hits&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&work_search%5Bcomplete%5D=0&tag_id=Sherlock+%28TV%29',
#       'http://archiveofourown.org/tags/Sherlock%20(TV)/works?commit=Sort+and+Filter&page=2&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Sherlock%20(TV)/works?commit=Sort+and+Filter&page=3&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Sherlock%20(TV)/works?commit=Sort+and+Filter&page=4&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
#       'http://archiveofourown.org/tags/Sherlock%20(TV)/works?commit=Sort+and+Filter&page=5&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits']

#dr who
url = ['http://archiveofourown.org/works?utf8=%E2%9C%93&commit=Sort+and+Filter&work_search%5Bsort_column%5D=hits&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&work_search%5Bcomplete%5D=0&tag_id=Doctor+Who+*a*+Related+Fandoms',
       'http://archiveofourown.org/tags/Doctor%20Who%20*a*%20Related%20Fandoms/works?commit=Sort+and+Filter&page=2&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
       'http://archiveofourown.org/tags/Doctor%20Who%20*a*%20Related%20Fandoms/works?commit=Sort+and+Filter&page=3&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
       'http://archiveofourown.org/tags/Doctor%20Who%20*a*%20Related%20Fandoms/works?commit=Sort+and+Filter&page=4&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits',
       'http://archiveofourown.org/tags/Doctor%20Who%20*a*%20Related%20Fandoms/works?commit=Sort+and+Filter&page=5&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=hits']




#%% grab all the data from the urls

df = pd.DataFrame()
#print(url)
for each in url:
    #print(each)    
    df = df.append(fd.get_data(each))
    
#df.head()
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, 'DrWho_11_10_17')
writer.save()

#%% connect to the database
#connstr = (
#    r"driver={microsoft access driver (*.mdb, *.accdb)};"
#    r"dbq=e:\\ao3stats\\ao3.accdb;"
#    )
#cnxn = pyodbc.connect(connstr)
#cursor = cnxn.cursor()
