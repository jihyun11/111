from importlib.resources import contents
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import date
import pymysql

nowDate=date.today().isoformat()
nowTime=datetime.now().time().isoformat()

df = pd.DataFrame(columns=['제목','내용','댓글수','글쓴이','날짜','조회수','추천수'])



def OnedayScrapping():
    start = 1
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')

    driver = webdriver.Chrome(r'C:\Users\Grail\Desktop\WorkSpace\Project\API\chromedriver.exe', options=options)
    check=""

    conn = pymysql.connect(host='localhost', user='root', password='qwer1234!A', charset='utf8', db='crawl_data') 
    cur = conn.cursor() 
    cur.execute("CREATE TABLE commu (commu_code int(15) NOT NULL AUTO_INCREMENT primary key, title varchar(20), contents varchar(500), comment varchar(200), writer varchar(20), date varchar(20), view varchar(200), rec varchar(200));")
    while "." not in check:
        print(start)
        url=f'https://www.fmkorea.com/index.php?mid=stock&page={start}'
        driver.get(url)
        driver.implicitly_wait(5)
        check=driver.find_element_by_xpath('//*[@id="bd_192159903_0"]/div/table/tbody/tr[5]/td[4]').text
        print(check)
        
        for count in range(5,6): #25
            com=[]
            target =driver.find_element_by_xpath(f'//*[@id="bd_192159903_0"]/div/table/tbody/tr[{count}]/td[2]/a')
            target.send_keys(Keys.COMMAND +"\n") 
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(3)
            
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[1]/h1/span').text)#제목
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[2]/article').text)#내용
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[3]/b').text)#댓글수
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[1]/a').text)#작성자
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[1]/span').text)#날짜
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[1]/b').text)#조회수
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[2]/b').text)#추천수
            print(com)

            sql = "INSERT INTO commu (title, contents, comment, writer, date, view, rec) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (com[0], com[1], com[2], com[3], com[4], com[5], com[6])
            
            cur.execute(sql)
            conn.commit()


            df.loc[len(df)] = com
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.implicitly_wait(1)
            
        driver.implicitly_wait(20)
        start =start+1

OnedayScrapping()





def DatasetScrapping():
    start = 200
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')

    driver = webdriver.Chrome(executable_path='/Applications/chromedriver', options=options)
    check=""
    for i in range(10000):
        print(start)
        url=f'https://www.fmkorea.com/index.php?mid=stock&page={start}'
        driver.get(url)
        driver.implicitly_wait(5)
        check=driver.find_element_by_xpath('//*[@id="bd_192159903_0"]/div/table/tbody/tr[5]/td[4]').text
        print(check)
        
        for count in range(5,6):#25
            com=[]
            target =driver.find_element_by_xpath(f'//*[@id="bd_192159903_0"]/div/table/tbody/tr[{count}]/td[2]/a')
            target.send_keys(Keys.CONTROL +"\n") 
            driver.switch_to.window(driver.window_handles[5])
            driver.implicitly_wait(3)
            
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[1]/h1/span').text)#제목
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[2]/article').text)#내용
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[3]/b').text)#댓글수
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[1]/a').text)#작성자
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[1]/span').text)#날짜
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[1]/b').text)#조회수
            com.append(driver.find_element_by_xpath('//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[2]/span[2]/b').text)#추천수
            print(com)
            df.loc[len(df)] = com
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.implicitly_wait(1)
            
        driver.implicitly_wait(20)
        start =start+1