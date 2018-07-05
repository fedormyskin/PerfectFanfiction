# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:48:07 2017

Analysing what people read on AO3


@author: SpaceyJo
"""
#%% Import Libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np


#%% Grab the ULS of the top 1-- fics by hits for Marvel

aothree = "https://archiveofourown.org"      
fandomcates = ['https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms', 
               'https://archiveofourown.org/media/Books%20*a*%20Literature/fandoms', 
               'https://archiveofourown.org/media/Cartoons%20*a*%20Comics%20*a*%20Graphic%20Novels/fandoms', 
               'https://archiveofourown.org/media/Celebrities%20*a*%20Real%20People/fandoms', 
               'https://archiveofourown.org/media/Movies/fandoms', 
               'https://archiveofourown.org/media/Music%20*a*%20Bands/fandoms', 
               'https://archiveofourown.org/media/Other%20Media/fandoms', 
               'https://archiveofourown.org/media/Theater/fandoms', 
               'https://archiveofourown.org/media/TV%20Shows/fandoms', 
               'https://archiveofourown.org/media/Video%20Games/fandoms', 
               'https://archiveofourown.org/media/Uncategorized%20Fandoms/fandoms']




#%%

def get_list_from_fandom_page(category):

        r = requests.get(category)
        soup = BeautifulSoup(r.content, 'lxml')

        body = soup.find('body')
        index = body.find('div', attrs={"id":"main"})
        fandoms = index.find('ol')

        boxes = fandoms.find_all('li', attrs = {'class':'letter listbox group'})

        urls = []
        for letter in boxes:
                fandom = letter.find_all('li')
                for each in fandom:
                        url = each.find('a', attrs={'class':'tag'})
                        urls.append(aothree+url['href'])
                        
        return urls

#%%

def get_fandoms_from_page():

        r = requests.get("https://archiveofourown.org/media")
        soup = BeautifulSoup(r.content, 'lxml')

        foo = soup.find('body')
        #bar = foo.find('div', attrs={'id':'outer'})
        #foobar = bar.find('div', attrs={'id':'inner'})
        #fooobaar = foobar.find('div', attrs = {'id':'main'})
        
        fandomboxes = foo.find('ul', attrs={'class':'media fandom index group'})
        fandomboxes2 = fandomboxes.find_all('li', attrs={'class' : 'medium listbox group'})
        fandomurls = []
        for each in fandomboxes2:
                url = each.find('a')
                fandomurls.append(aothree+url['href'])
                
        return fandomurls

#%% Create me a function!
def get_works_from_page(soup):

        main_body = soup.find('ol', attrs={'class':'work index group'})
        works_raw = main_body.find_all('li', attrs={'class':'work blurb group'})
        w_dict = {}
        if works_raw: # if there are works on the page then do the work
                df = pd.DataFrame()
                for work in works_raw:
                        
                        header = work.find('h4')
                        w_title = header.find('a').contents[0]

                        #authors
                        w_author = []
                        raw_authors = header.find_all('a', attrs={'rel':'author'})
                        for author in raw_authors:
                                w_author.append(author.contents[0])

                        #fandoms
                        fandom_heading = work.find('h5')
                        w_fandom =[]
                        raw_fandoms = fandom_heading.find_all('a', attrs={'class':'tag'})
                        for fandom in raw_fandoms:
                                w_fandom.append(fandom.contents[0])

                        tag_header = work.find('ul', attrs={'class':'tags commas'})

                        #Warnings
                        warnings = tag_header.find_all('li', attrs={'class':'warnings'})
                        w_warnings = []
                        for warn in warnings:
                                raw_warn = warn.find('a')
                                w_warnings.append(raw_warn.contents[0]) 
                        #pairings
                        pairings = tag_header.find_all('li', attrs={'class':'relationships'})
                        w_pairings = []
                        for pair in pairings:
                                raw_pair = pair.find('a').contents[0]
                                w_pairings.append(raw_pair)

                         #characters
                        characters = tag_header.find_all('li', attrs={'class':'characters'})
                        w_chars = []
                        for char in characters:
                                raw_char = char.find('a').contents[0]
                                w_chars.append(raw_char)

                        #freeforms
                        freeform = tag_header.find_all('li', attrs={'class':'freeforms'})
                        w_freeform = []
                        for free in freeform:
                                raw_free = free.find('a').contents[0]
                                w_freeform.append(raw_free)
 
                        #ADD EXCEPTIONS FOR EVERY CASE WHERE THERE MAY NOT BE A STAT!     
 
                        #stats
                        stats = work.find('dl', attrs={'class':'stats'})

                        #words
                        w_words = stats.find('dd', attrs={'class':'words'}).contents[0]

                        #chapters
                        w_chaps = stats.find('dd', attrs={'class':'chapters'}).contents[0]

                        #Comments
                        if stats.find('dd', attrs={'class':'comments'}):
                                w_comments = stats.find('dd', attrs={'class':'comments'}).a.contents[0]
                        else:
                                w_comments = np.nan
                        #kudos
                        if stats.find('dd', attrs={'class':'kudos'}):
                                w_kudos = stats.find('dd', attrs={'class':'kudos'}).a.contents[0]
                        else:
                                w_kudos = np.nan

                        #bookmarks
                        if stats.find('dd', attrs={'class':'bookmarks'}):
                                w_bookmark = stats.find('dd', attrs={'class':'bookmarks'}).a.contents[0]
                        else:
                                w_bookmark = np.nan

                        #hits
                        if stats.find('dd', attrs={'class':'hits'}):
                                w_hits = stats.find('dd', attrs={'class':'hits'}).contents[0]
                        else:
                                w_hits = np.nan

                        w_dict = {'Title': w_title, 'Authors':w_author, 'Fandoms':w_fandom, \
                                   'Warnings':w_warnings, 'Pairings': w_pairings, \
                                   'Characters':w_chars ,'Freeforms':w_freeform, \
                                   'Words':w_words, 'Chapters':w_chaps,\
                                   'Kudos':w_kudos, 'Bookmarks':w_bookmark, 'Hits':w_hits, \
                                   'Comments':w_comments}
        
                        df = df.append(w_dict, ignore_index = True)
       
        return df
#%%


