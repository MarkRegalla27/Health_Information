import requests
from bs4 import BeautifulSoup
#import re
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#import matplotlib.pyplot as plt
import mpld3
import os
import codecs
#import gensim
#from gensim import corpora, models, similarities
import logging
import os

def do_my_func(aString):
    #aString = 'A ' + aString + ' is bad, mkay.'
    
    #Scrape Wikipedia
    response = requests.get('https://en.wikipedia.org/wiki/Myocardial_infarction')
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    paragraphs = soup.findAll('p')
    k = 0
    theindex = 0
    foundone = False
    for i in paragraphs:
        if 'heart attack' in paragraphs[k].text:
            if foundone == False:
                theindex = k
                foundone = True
        k += 1
    wikidef = paragraphs[theindex].text
    wikisentences = sent_tokenize(wikidef)

    #Scrape WebMD
    response2 = requests.get('http://www.webmd.com/heart-disease/guide/heart-disease-heart-attacks')
    page2 = response2.text
    soup2 = BeautifulSoup(page2, 'html.parser')
    paragraphs2 = soup2.findAll('p')
    k = 0
    theindex2 = 0
    foundone2 = False
    for i in paragraphs2:
        if 'heart attack' in paragraphs2[k].text:
            if foundone2 == False:
                theindex2 = k
                foundone2 = True
        k += 1
    webmddef = paragraphs2[theindex2].text
    webmdsentences = sent_tokenize(webmddef)

    #Scrape MayoClinic
    response3 = requests.get('http://www.mayoclinic.org/diseases-conditions/heart-attack/basics/definition/con-20019520')
    page3 = response3.text
    soup3 = BeautifulSoup(page3, 'html.parser')
    paragraphs3 = soup3.findAll('p')
    k = 0
    theindex3 = 0
    foundone3 = False
    for i in paragraphs3:
        if 'heart attack' in paragraphs3[k].text:
            if foundone3 == False:
                theindex3 = k
                foundone3 = True
        k += 1
    mayodef = paragraphs3[theindex3].text
    mayosentences = sent_tokenize(mayodef)

    #Jaccard Similarity
    wikiset = set(wikidef)
    webmdset = set(webmddef)
    mayoset = set(mayodef)

    theintersect = wikiset.intersection(webmdset)
    theintersect = theintersect.intersection(mayodef)
    theunion = wikiset.union(webmdset)
    theunion = theunion.union(mayodef)

    theintersect_len = len(list(theintersect))
    theunion_len = len(list(theunion))

    jaccard = float(theintersect_len) / theunion_len

    if jaccard > 0.5:
        aString = 'Definitions Match.\n'
        aString = aString + 'MayoClinic Definition (as confirmed by WebMD and Wikipedia):\n'
        aString = aString + mayodef
    else:
        aString = 'Conflicting Definitions.'

    return aString

#print do_my_func('heart attack')
