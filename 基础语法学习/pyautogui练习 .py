import pyautogui

# 获取当前屏幕分辨率
x,y  = pyautogui.size()

# 获取当前鼠标位置
mX, mY = pyautogui.position()
print(x,y)
print(mX,mY)
pyautogui.click()
pyautogui.typewrite('123456',interval=1)
pyautogui.typewrite(['a','left','b'],interval=1)
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])

