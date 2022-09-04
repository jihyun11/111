from bs4 import BeautifulSoup
import requests
import re

date = input("날짜를 입력해 주세요: ")
url = "http://finance.naver.com/news/news_list.nhn?"
params = {'mode' : 'RANK', 'date' : date}

resp = requests.get(url, params)
print(resp)

soup = BeautifulSoup(resp.content, 'lxml')


url_list = soup.find('div', 'hotNewsList').find_all('a')
news_url_list = []

for url in url_list :
    news_url_list.append('https://finance.naver.com') + url['href']

print(len(news_url_list))
news_url_list[0]

def get_news_by_url(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}
    res = request.get(url, headers = headers)
    bs = BeautifulSoup(res.content, 'html.parser')

    title = bs.find('div', 'article_info').find('h3').string
    title = re.sub('\t|\r|\n| ', '', title)
    content = bs.find('div', 'articleCont').text
    content = re.sub('\xa0|\t|\r|\n|', '', content)

    return title + content

    news_content = []
    for url in news_url_list :
        neww_content.append(get_news_by_url(url))

    news_content[10]