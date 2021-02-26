import requests as rq#导入需要的requests包
import re #导入正则表达式需要的包
import os
response=rq.get('http://www.mingzhuxiaoshuo.com/waiguo/150/')#向网站发出请求，获取返回信息
response.encoding='gbk'
html=response.text#获取目标url源码
#print(html)#看看结果是怎样的
title=re.findall(r'<div id="title"><h1>(.*?)</h1>',html)[0]
author=re.findall(r'<a href=".*">(.*?)</a>',html)[1]
# print(title)
# print(author)

dq=os.getcwd()
dir1=dq+'\\'+title
if not os.path.exists(dir1):
    os.mkdir(dir1)#为当前小说创建一个文件夹

juanName=re.findall(r'<div class="list"> <div class="title"><span>(.*?)</span></div>',html)[0]
#print(juanName)
dir2=dir1+'\\'+juanName
if not os.path.exists(dir2):
    os.mkdir(dir2)#为分卷创建一个文件夹

dl=re.findall(r'<li><a href=(.*?)</a></li>',html,re.S)
#print(dl)
j=1000
for i in dl:
    #print(i)
    url_html=re.findall(r'"(.*?)" target',i)#获取目标章节的网址链接
    #print(url_html)
    chapterName=re.findall(r'title="(.*?)">',i)#获取目标章节的名称
    #print(chapterName)
    dir3=dir2+'\\'+str(j)+chapterName[0]
    j=j+1
    url='http://www.mingzhuxiaoshuo.com/'+url_html[0]
    chapter_response = rq.get(url)
    chapter_response.encoding = 'gbk'
    chapter_html = chapter_response.text
    chapter_response.close()
    #print(chapter_html)
    content=re.findall(r'<div class="width">(.*?)</div>',chapter_html,re.DOTALL)[0]
    #print(content)
    content = content.replace('\r\n\r\n<script src="Http://www.mingzhuxiaoshuo.com/AD/Contents.JS"></script>\r\n\r\n<p>', '')
    content = content.replace('<div style="height:5px">', '')
    content = content.replace('<p>', '')
    content = content.replace('</p>', '')
    content = content.replace('&nbsp;', '') #print(content)
    if not os.path.exists(dir3):
        fb = open('%s.txt' % dir3, 'w', encoding='utf-8')
        fb.write(content)
    print(url,chapterName)