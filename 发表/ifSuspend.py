import requests as rq
import io
import time
import sys
import os
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码
browser = webdriver.PhantomJS('C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
url=r'http://ymiir.top'
browser.get(url)
browser.implicitly_wait(3)
browser.save_screenshot('screenshouts\\picture10.png')
username = browser.find_element_by_name('username')
username.send_keys('yoonamessi')
password = browser.find_element_by_name('password')
password.send_keys('thenight123')
login_button = browser.find_element_by_name('submit')
login_button.submit()
time.sleep(5)
browser.save_screenshot('screenshouts\\picture11.png')
author_tool=browser.find_element_by_xpath('//*[@id="jieqi_menu"]/li[5]/a').click()
browser.implicitly_wait(3)
browser.save_screenshot('screenshouts\\picture12.png')
browser.find_element_by_xpath('//*[@id="left"]/div[1]/div[2]/ul/li[6]/a').click()
browser.save_screenshot('screenshouts\\picture13.png')

# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])  # 此行代码用来定位当前页面


browser.find_element_by_xpath('//*[@id="checkform"]/table/tbody/tr[4]/td[1]/a').click()
windows = browser.current_window_handle #定位当前页面句柄
all_handles = browser.window_handles   #获取全部页面句柄
for handle in all_handles:
    print(handle.title())
print('*************************')
for handle in all_handles:          #遍历全部页面句柄
    if handle != windows:          #判断条件
        browser.switch_to.window(handle)      #切换到新页面
print(browser.title)


browser.save_screenshot('screenshouts\\picture14.png')
browser.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a[1]').click()
browser.save_screenshot('screenshouts\\picture15.png')
articlename='权力的游戏'
juanming='正文'
novel_list=os.listdir('..\\爬取\\'+articlename+'\\'+juanming)
novel_list=novel_list[41:]
for i in novel_list:
    browser.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[1]/td/a[2]').click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="chaptername"]').send_keys(i)
    fb=open('..\\爬取\\'+articlename+'\\'+juanming+'\\'+i,'r',encoding='utf-8')
    content=fb.read()
    browser.find_element_by_xpath('//*[@id="chaptercontent"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="submit"]').submit()
    time.sleep(5)