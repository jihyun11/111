import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime

basic_url = "https://finance.naver.com/sise/"

fp = urllib.request.urlopen(basic_url)

source = fp.read()

fp.close()

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("span",class_="num")


kospi_value = soup[0].string
kosdaq_value = soup[1].string
#print(soup)

print(kospi_value)
print(kosdaq_value)