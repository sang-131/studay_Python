# 本地Chrome浏览器的静默默模式设置：
from selenium import  webdriver 
#从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options
# 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') 
chrome_options.add_argument('–disable-gpu')
chrome_options.add_argument('log-level=3')
# 把Chrome浏览器设置为静默模式,禁止打印日志
#driver = webdriver.Chrome(options = chrome_options) 
driver = webdriver.Chrome() 
# 设置引擎为Chrome，在后台默默运行
driver.get('https://ibank.ubagroup.com/eng/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=GH&LANGUAGE_ID=001') 
# 访问页面
time.sleep(2)

comments = driver.find_element_by_class_name('type_UserPrincipal').send_keys('WANHENG.YAN') # 使用class_name找到评论
driver.find_element_by_class_name('waves-effect').click()

time.sleep(2) # 等待一秒

pageSource = driver.page_source
print(pageSource)

driver.close() # 关闭浏览器