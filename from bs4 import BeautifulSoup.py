import urllib.request
from bs4 import BeautifulSoup

# 네이버 금융 국내증시 메인 사이트 주소
url = "https://finance.naver.com/sise/"

# 웹사이트 정보 요청
page = urllib.request.urlopen(url)

# 해당 페이지는 cp949 방식의 인코딩 사용
html = page.read().decode('cp949')

# html.parser로 html 형식 태그에서 데이터 추출 준비
soup = BeautifulSoup(html, 'html.parser')

soup.select('span.num')


