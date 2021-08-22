from selenium import  webdriver 
import time

driver = webdriver.Chrome() 
# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') 
# time.sleep(2)

# teacher = driver.find_element_by_id('teacher')
# teacher.send_keys('必须是吴枫呀')
# assistant = driver.find_element_by_name('assistant')
# assistant.send_keys('都喜欢')
# time.sleep(1)
# button = driver.find_element_by_class_name('sub')
# time.sleep(1)
# button.click()
# time.sleep(1)
# driver.close()


# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
# time.sleep(2) # 等待2秒

# label = driver.find_element_by_tag_name('label') # 解析网页并提取第一个<label>标签中的文字
# print(type(label)) # 打印label的数据类型
# print(label.text) # 打印label的文本
# print(label) # 打印label
# driver.close() # 关闭浏览器
# from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# import time

# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)
log=driver.find_element_by_name('log')
log.send_keys('sang')
pwd=driver.find_element_by_name('pwd')
pwd.send_keys('sang131ass')
submint=driver.find_element_by_name('wp-submit')
submint.click()
time.sleep(2)
a =driver.find_element_by_partial_link_text('未来已来（三）')
a.click()
time.sleep(2)
comment=driver.find_element_by_name('comment')
comment.send_keys('selenium,点点成功')
sub=driver.find_element_by_name('submit')
sub.click()
driver.close()