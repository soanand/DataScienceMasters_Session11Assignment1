"""
Created on Wed Jul 11 18:52:15 2018

@author: soanand

Problem Statement

In this assignment students have to find the frequency of words in a webpage. User can
use urllib and BeautifulSoup to extract text from webpage.

Hint:
from bs4 import BeautifulSoup
import urllib.request
import nltk

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source​ ​code​ ​used​ ​and
"""

from bs4 import BeautifulSoup
import urllib
from collections import Counter
import nltk
try:
    #Get data from url 'http://php.net/'
    response = urllib.request.urlopen('http://php.net/')
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
     
    #Extract the text from web page
    text = soup.get_text(strip=True)
    
    #Split the text using space
    tokens = [t for t in text.split()]
    
    #COunt the frequecncy of word
    freq = nltk.FreqDist(tokens)
    
    #To write the output into text file
    with open('result.txt','w') as f:
        for key,val in freq.items():
            f.write(str(key) + ':' + str(val)+'\n')
            
except Exception as e:
    print(e)
