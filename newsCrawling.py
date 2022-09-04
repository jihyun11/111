from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pymysql



driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://finance.naver.com/news/'
driver.get(url)



#test1=driver.find_element(by=By.XPATH, value='//*[@id="newarea"]/div[1]/ul/li[1]').click()
test1=driver.find_element(by=By.XPATH, value='//*[@id="newarea"]/div[1]/ul/li[1]/a/strong').click()

conn = pymysql.connect(host='localhost', user='root', password='qwer1234!A', charset='utf8', db='crawl_data') 
cur = conn.cursor()
cur.execute("create table news (news_code int(15) NOT NULL AUTO_INCREMENT primary key, title varchar(50),content varchar(1000),date varchar(20),press varchar(20));")

for j in range(2,10):

    for i in range(1, 11):
        test1=driver.find_element(by=By.XPATH, value=f'//*[@id="contentarea_left"]/ul/li[1]/dl/dt[{i}]/a').click()
        print(test1)
        driver.implicitly_wait(2)
        test2=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[2]/div[1]/div[2]/h3').text #title
        test3=driver.find_element(by=By.XPATH, value='//*[@id="content"]').text #content
        test4=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[2]/div[1]/div[2]/div/span').text #date
        test5=driver.find_element(by=By.CLASS_NAME, value="press")
        test6=test5.find_element_by_tag_name("img")
        test7=test6.get_attribute("alt") #press

        sql = "INSERT INTO news (title, content, date, press) VALUES ('%s', '%s', '%s', '%s')" % (test2, test3, test4, test7)
            
        cur.execute(sql)
        
        
        driver.back() #뒤로가기
        driver.implicitly_wait(2)
    for i in range(1, 11):
        test1=driver.find_element(by=By.XPATH, value=f'//*[@id="contentarea_left"]/ul/li[2]/dl/dt[{i}]/a').click()
        print(test1)
        driver.implicitly_wait(2)
        test8=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[2]/div[1]/div[2]/h3').text #title
        test9=driver.find_element(by=By.XPATH, value='//*[@id="content"]').text #content
        test10=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[2]/div[1]/div[2]/div/span').text #date
        test11=driver.find_element(by=By.CLASS_NAME, value="press")
        test12=test5.find_element_by_tag_name("img")
        test13=test6.get_attribute("alt") #press
        

        sql = "INSERT INTO news (title, content, date, press) VALUES ('%s', '%s', '%s', '%s')" % (test8, test9, test10, test13)
            
        cur.execute(sql)
        conn.commit()
        
        driver.back() #뒤로가기
        driver.implicitly_wait(2)
    url=f"https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258&page={j}"
    driver.get(url)
    

