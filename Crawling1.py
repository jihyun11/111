from optparse import Values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pymysql


driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
url = 'https://finance.naver.com'
driver.get(url)

test1=driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[2]/a').click()
test0=driver.find_element(by=By.XPATH, value='//*[@id="contentarea"]/div[1]/div[1]/ul/li[1]').click()
test2=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[1]/h3').text #제목
test3=driver.find_element(by=By.XPATH, value='//*[@id="now_value"]').text #숫자
test4=driver.find_element(by=By.XPATH, value='//*[@id="change_value_and_rate"]').text #증감
print(test2, test3, test4)
#코스피

test1=driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[2]/a').click()
test0=driver.find_element(by=By.XPATH, value='//*[@id="contentarea"]/div[1]/div[1]/ul/li[2]').click()
test5=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[1]/h3').text #제목
test6=driver.find_element(by=By.XPATH, value='//*[@id="now_value"]').text #숫자
test7=driver.find_element(by=By.XPATH, value='//*[@id="change_value_and_rate"]').text #증감
print(test5, test6, test7)
#코스닥

test1=driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[2]/a').click()
test0=driver.find_element(by=By.XPATH, value='//*[@id="contentarea"]/div[1]/div[1]/ul/li[3]').click()
test8=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[1]/h3').text #제목
test9=driver.find_element(by=By.XPATH, value='//*[@id="now_value"]').text #숫자
test10=driver.find_element(by=By.XPATH, value='//*[@id="change_value"]').text #전일대비
test11=driver.find_element(by=By.XPATH, value='//*[@id="change_rate"]').text #등락율
print(test8, test9, test10, test11)
#코스피200




conn = pymysql.connect(host='localhost', user='root', password='qwer1234!A', charset='utf8', db='crawl_data')
cur = conn.cursor()

cur.execute("CREATE TABLE crawll (name varchar(20), id varchar(20), height varchar(20))")

sql = "INSERT INTO crawll (name, id, height) VALUES (%s, %s, %s)"
val = ((test2, test3, test4))

cur.execute(sql, val)
conn.commit()

sql1 = "INSERT INTO crawll (name, id, height) VALUES (%s, %s, %s)"
val1 = ((test5, test6, test7))
cur.execute(sql1, val1)
conn.commit()

sql2 = "INSERT INTO crawll (name, id, height) VALUES (%s, %s, %s)"
val2 = ((test8, test9, test11))
cur.execute(sql2, val2)
conn.commit()


conn.close()
