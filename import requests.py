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

#top_trades=soup.find_all("div", attrs={"class":"title"})
#for top_trade in top_trades:
    #print(top_trade.get_text()) 


url = "https://finance.naver.com"
res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
print(soup.title)

soup.find(attrs={"class":"tbl_home"})
finance_rankhigh=(soup.find(attrs={"class":"tbl_home"}))
print(finance_rankhigh.get_text()) 