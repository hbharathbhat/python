# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:24:19 2024

@author: hbharathbhat
"""

from bs4 import BeautifulSoup
import requests


page_to_scrape=requests.get("https://quotes.toscrape.com")
soup=BeautifulSoup(page_to_scrape.text,"html.parser")
quotes=soup.findAll("span",attrs={"class":"text"})
authors=soup.findAll("small",attrs={"class":"author"})
tags=soup.findAll("small",attrs={"class":"tag"})

for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)
for tag in tags:
    print(tag.text)
