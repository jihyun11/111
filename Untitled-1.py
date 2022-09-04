import requests
from bs4 import BeautifulSoup

#financenews

url = "https://finance.naver.com/news/mainnews.naver"
res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
print(soup.title)

soup.find(attrs={"class":"mainNewsList"})
finance_news=(soup.find(attrs={"class":"mainNewsList"}))
print(finance_news.get_text()) 



#finance

url = "https://finance.naver.com"
res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
print(soup.title)

soup.find("div", attrs={"class":"heading_area"}) #section_stock
finance=(soup.find("div", attrs={"class":"heading_area"}))
print(finance.get_text()) 

 












