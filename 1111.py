from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
url = 'https://finance.naver.com'
driver.get(url)

#test=driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a/span/span[1]').text
#test2=driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a/span/span[2]').text
#test3=driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/h4').text


#test1=driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/h4/a/em/span').text
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

test1=driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[7]/a').click()
test2=driver.find_element(by=By.XPATH, value='//*[@id="newsMainTop"]/div/div[1]/h4').text #제목
test3=driver.find_element(by=By.XPATH, value='//*[@id="newsMainTop"]/div/div[1]/div/div[1]').text #기사...내용
print(test2, test3)
#뉴스

test1=driver.find_element(by=By.XPATH, value='//*[@id="newarea"]/div[1]/ul/li[2]/a').click()
test4=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/h3').text #제목
test5=driver.find_element(by=By.XPATH, value='//*[@id="contentarea_left"]/div[2]').text #내용
print(test4, test5)
#주요뉴스








#driver.implicitly_wait(10)
#print(test1)
#i=0
#while True:
#    test1=driver.find_element(by=By.XPATH, value='//*[@id="popularItemList"]/li[{i}]/a').text
#    i=+1
#    if i
# print(test,test1)