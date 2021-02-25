import requests as rq#导入需要的requests包
import re #导入正则表达式需要的包
import os
response=rq.get('http://www.mingzhuxiaoshuo.com/waiguo/150/')#向网站发出请求，获取返回信息
response.encoding='gbk'
html=response.text#获取目标url源码
#print(html)#看看结果是怎样的
title=re.findall(r'<div id="title"><h1>(.*?)</h1>',html)[0]
author=re.findall(r'<a href=".*">(.*?)</a>',html)[1]
print(title)
print(author)

dq=os.getcwd()
os.mkdir(dq+'\\'+title)#为当前小说创建一个文件夹
dir1=dq+'\\'+title

juanName=re.findall(r'<div class="list"> <div class="title"><span>(.*?)</span></div>',html)[0]
print(juanName)
os.mkdir(dir1+'\\'+juanName)
dir2=dir1+'\\'+title

dl=re.findall(r'<div id="list">.*?</div>',html,re.S)
