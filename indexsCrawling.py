from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pymysql



driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://finance.naver.com/sise/'
driver.get(url)



conn = pymysql.connect(host='localhost', user='root', password='qwer1234!A', charset='utf8', db='crawl_data') 
cur = conn.cursor()
#cur.execute("CREATE TABLE indexs (index_code int(15) NOT NULL AUTO_INCREMENT primary key, name varchar(20),date varchar(15), id varchar(20), height varchar(20),subject varchar(20));")

#1 지수


for h in range(1, 4):
    test1=driver.find_element(by=By.XPATH, value=f'//*[@id="contentarea"]/div[1]/div[1]/ul/li[{h}]/a').click() #코스피로 넘어가기
    test2=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[1]/h3').text #title

    for j in range(1, 11):
        test1=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[2]/tbody/tr/td[{j}]/a').click()
        driver.implicitly_wait(2)

        for i in range(3, 13):
            test3=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[1]').text #date
            test4=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[2]').text #id
            test5=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[4]/span').text #hight
            test6="지수"
       
        sql = "INSERT INTO indexs (name, date, id, hight, subject) VALUES ('%s', '%s', '%s', '%s', '%s')" % (test2, test3, test4, test5, test6)
            
        cur.execute(sql)
        cur.commit()

        test1=driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[2]/a/span').click

        #driver.back() #뒤로가기
        #driver.implicitly_wait(2)


#2 환율

driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW'
driver.get(url)


for j in range(1, 11):
        test1=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[2]/tbody/tr/td[{j}]/a').click() #페이지네이션
        driver.implicitly_wait(2)

        for i in range(1, 11):
            test3=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[1]').text #date
            test4=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[2]').text #id
            test5=driver.find_element(by=By.XPATH, value=f'/html/body/div/table[1]/tbody/tr[{i}]/td[4]/span').text #hight
            test6="환율"
       
        sql = "INSERT INTO indexs (name, date, id, hight, subject) VALUES ('%s', '%s', '%s', '%s', '%s')" % (test2, test3, test4, test5, test6)
            
        cur.execute(sql)
        cur.commit()


        #driver.back() #뒤로가기
        #driver.implicitly_wait(2)





    