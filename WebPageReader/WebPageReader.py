
import requests;
import bs4 as soup;
import html2text;
import pathlib;
import urllib3.request as u3_request;
import string
import re
import io
from collections import defaultdict
import heapq 

def getPageFromWeb(url):
    """
    Get webpage content and return HTML
    """
    pageInfo = requests.get(url)
    status = pageInfo.status_code

    return pageInfo,status



def getKeyWords(htmlDocument):
    """
    Reads a html document's metadata tags for keywords
    """
    contentConstant = "<meta content=\""
    endTag = "\" itemid"
    contentConstantLength = len(contentConstant)

    souped = soup.BeautifulSoup(pageInfo.text,'html.parser').head

    kw = souped.find('meta',attrs={'name' : 'keywords'}).prettify()

    stringStart = kw.rfind(contentConstant)+contentConstantLength
    stringEnd = kw.rfind(endTag)

    justTheTags = kw[stringStart:stringEnd]

    tagsArray = justTheTags.split(",")

    return tagsArray;

def countWordFrequencyInString(str):
    str = stripStringOfPunctuation(str)

    counts = dict()

    words = str.lower().split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts

def pageToText(url):

    text =""
    html = requests.get(url);

    status = html.status_code;

    if (status == 200):
        text = html2text.html2text(html.text)

    return text


def readOfflinePage(location):
    file = io.FileIO(location,'r')

    result = file.read()
    return result

def stripStringOfPunctuation(text):
    result = re.sub(r"""
               [-”“(),.;@#?!&$]+  # Accept one or more copies of punctuation
               \ *           # plus zero or more copies of a space,
               """,
               " ",          # and replace it with a single space
               text, flags=re.VERBOSE)
    return result;

def isolateBodyFromHTML(htmlDocument):
    souped = soup.BeautifulSoup(htmlDocument,'html.parser').body
    return souped.text;

def returnTop3DictionaryEntries(dictionary):
    keys = heapq.nlargest(3,dictionary,key=dictionary.get)
    result = {'':''}
    for key in keys:
        result[key]=dictionary.get(key)
    return result

def stripDictionaryOfArticles(dictionary):
    exclusionList = {"a","the","to","of","and","that","in","for","is","as","are","an","with"}
    for word in exclusionList:
        dictionary.pop(word,None)
    return dictionary


