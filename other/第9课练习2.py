from selenium import  webdriver 
import time

from bs4 import BeautifulSoup

driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher=driver.find_element_by_name('teacher')
teacher.send_keys('吴枫呀')
assistant=driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
button=driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)
# words=driver.find_elements_by_id('p')
# for i in words:
#     print(i.text)
# driver.close()    
pagesource=driver.page_source
soup = BeautifulSoup(pagesource,'html.parser')
soup=soup.find_all('p',id='p')
a=0
#print(len(soup))
for i in soup:  
    print(type(i))
    print(i.text)
    print(type(i.text))
driver.close()    
