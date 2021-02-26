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
username = browser.find_element_by_name('username')
username.send_keys('yoonamessi')
password = browser.find_element_by_name('password')
password.send_keys('thenight123')
login_button = browser.find_element_by_name('submit')
login_button.submit()
browser.save_screenshot('screenshouts\\picture1.png')
time.sleep(4)
author_tool=browser.find_element_by_xpath('//*[@id="jieqi_menu"]/li[5]/a').click()
browser.implicitly_wait(3)
browser.save_screenshot('screenshouts\\picture2.png')
author_tool=browser.find_element_by_xpath('//*[@id="left"]/div[1]/div[2]/ul/li[1]/a').click()
browser.implicitly_wait(3)
author_tool=browser.find_element_by_name('sortid').click()
author_tool=browser.find_element_by_xpath('//*[@id="sortid"]/option[11]').click()
browser.save_screenshot('screenshouts\\picture3.png')
articlename='权力的游戏'
browser.find_element_by_name('articlename').send_keys(articlename)
browser.find_element_by_name('agent').send_keys('yoonamessi')
browser.find_element_by_xpath('//*[@id="author"]').send_keys('乔治·R·R·马丁')
browser.find_element_by_name('notice').send_keys('已完结。')
browser.find_element_by_name('submit').submit()
browser.save_screenshot('screenshouts\\picture4.png')
time.sleep(10)
browser.implicitly_wait(3)
browser.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[1]/td/a[1]').click()
juanming='正文'
browser.find_element_by_xpath('//*[@id="chaptername"]').send_keys(juanming)
browser.find_element_by_xpath('//*[@id="submit"]').submit()
time.sleep(4)
novel_list=os.listdir('..\\爬取\\'+articlename+'\\'+juanming)
for i in novel_list:
    browser.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[1]/td/a[2]').click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="chaptername"]').send_keys(i)
    fb=open('..\\爬取\\'+articlename+'\\'+juanming+'\\'+i,'r',encoding='utf-8')
    content=fb.read()
    browser.find_element_by_xpath('//*[@id="chaptercontent"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="submit"]').submit()
    time.sleep(5)
