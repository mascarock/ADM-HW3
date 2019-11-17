import requests
import urllib.request
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import os


url = "https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies2.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movieslist = []

for tr in soup.findAll('tr'):
    for td in tr.findAll('td'):
        if "http" in (td.text):
            movieslist.append(td.text)
        
for i in range(9000,10000):
    time.sleep(3)
    response = urlopen(movieslist[i])
    namefile = "article_" + str(i+10000)+ ".html"
    with open(namefile, "wb") as f:
        f.write(response.read())
        f.close()
