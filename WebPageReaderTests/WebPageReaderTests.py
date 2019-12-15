import WebPageReader
import sys
import requests
from collections import defaultdict

def test_getPageFromWebReturnsSuccessWhenPresent():
    url = r"https://pythonbasics.org/multiple-return/"
    success = 200
    
    try: 
        page,status = WebPageReader.getPageFromWeb(url)
        if (status != success): raise ValueError
        else:
            print ("test_getPageFromWebReturnsSuccessWhenPresent passed")

    except ValueError:
        print("Unexpected URL error")
    
def test_getPageFromWebReturnsHttpResponse():
    url = r"https://pythonbasics.org/multiple-return/"
    try:
        page,status = WebPageReader.getPageFromWeb(url)
        if ((isinstance(page,requests.models.Response)) is False): raise ValueError
        else:
            print ("test_getPageFromWebReturnsHttpResponse passed")

    except ValueError:
        print("Unexpected return type")

def test_countWordFrequencyInStringCanCountSimpleStrings():
    text = "None of this has happened by chance. In 1999, the United States had free and competitive markets in many industries that, in Europe, were dominated by oligopolies. Today the opposite is true. French households can typically choose among five or more internet-service providers; American households are lucky if they have a choice between two, and many have only one. The American airline industry has become fully oligopolistic; profits per passenger mile are now about twice as high as in Europe, where low-cost airlines compete aggressively with incumbents."
    try:
        result = WebPageReader.countWordFrequencyInString(text)
        if (len(result)==0): raise ValueError
        else:
            print("test_countWordFrequencyInStringCanCountSimpleStrings passed")
    except ValueError:
        print("test_countWordFrequencyInStringCanCountSimpleStrings failed")

def test_countWordFrequencyInStringDoesNotDistinguishPropercasedWords():
    text="Dog dog"
    try:
        result = WebPageReader.countWordFrequencyInString(text)
        if(result["dog"]!=2):raise ValueError
        else:
            print("test_countWordFrequencyInStringDoesNotDistinguishPropercasedWords passed")
    except ValueError:
            print("test_countWordFrequencyInStringDoesNotDistinguishPropercasedWords failed")

def test_countWordFrequencyInStringDoesNotCountPunctuationSeparatedWordsAsASingleWord():
    text="Dog;dog"
    try:
        result = WebPageReader.countWordFrequencyInString(text)
        if(result.get('dog')!=2):raise ValueError
        else:
            print("test_countWordFrequencyInStringDoesNotCountPunctuationSeparatedWordsAsASingleWord passed")
    except ValueError:
            print("test_countWordFrequencyInStringDoesNotCountPunctuationSeparatedWordsAsASingleWord failed")

def test_stripStringOfPunctuationLeavesSpacesInResultingString():
    text="Dog;dog,joke;blog"
    expected = "Dog dog joke blog"
    try:
        result = WebPageReader.stripStringOfPunctuation(text)
        if(result != expected ):raise ValueError
        else:
            print("test_stripStringOfPunctuationLeavesSpacesInResultingString passed")
    except ValueError:
            print("test_stripStringOfPunctuationLeavesSpacesInResultingString failed")

def test_isolateBodyFromHTMLReturnsHTMLBodyOnly():
    fileLocation = r"C:\Files\Articles\Design Thinking Comes of Age.htm"
    page = WebPageReader.readOfflinePage(fileLocation)
    try:
        body = WebPageReader.isolateBodyFromHTML(page)
        print("test_isolateBodyFromHTMLReturnsHTMLBodyOnly passed")
    except ValueError:
        print("test_isolateBodyFromHTMLReturnsHTMLBodyOnly failed")
    
#testExcecution

#test_getPageFromWebReturnsSuccessWhenPresent()
#test_getPageFromWebReturnsHttpResponse()
#test_countWordFrequencyInStringCanCountSimpleStrings()
#test_countWordFrequencyInStringDoesNotDistinguishPropercasedWords()
#test_countWordFrequencyInStringDoesNotCountPunctuationSeparatedWordsAsASingleWord()
#test_isolateBodyFromHTMLReturnsHTMLBodyOnly()

#working area
result = WebPageReader.countWordFrequencyInString(WebPageReader.stripStringOfPunctuation(WebPageReader.isolateBodyFromHTML(WebPageReader.readOfflinePage(r"C:\Files\Articles\Design Thinking Comes of Age.htm"))))

for item in result:
    print(item + " "+ str(result.get(item)))

result = WebPageReader.stripDictionaryOfArticles(result)
result = WebPageReader.returnTop3DictionaryEntries(result)

for item in result:
    print(item + " " +str(result.get(item)))
