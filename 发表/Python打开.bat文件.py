import pyautogui as pg
import time
import pyperclip as pp
pg.PAUSE=1#每个函数执行后停顿1.5秒
w,h=pg.size() #获取屏幕尺寸
pg.hotkey('Win','r')
pg.press(['c','m','d'])
pg.press('enter')
pg.click(w/2,h/2,)
pg.typewrite('D:')
pg.press('enter')
pg.typewrite('cd Repositories')
pg.press('enter')
pg.typewrite('cd Automatic-crawling-and-publishing')
pg.press('enter')
pg.typewrite('openchrome.bat')
pg.press('enter')

pList=[]
f=open('inputP.txt','r',encoding='utf-8')
for line in f:
    pList.append(line.strip('\n'))
print(pList)
i=0
dict={}
while True:
    if pList[i]=='#':
        break
    dict[pList[i]]=pList[i+1]
    i=i+2
print(dict)
def click(str2):
    str1 = dict[str2]
    j = int(str1[1:4])
    k = int(str1[6:9])
    pg.click(j, k)
time.sleep(0.75)
for i in ['用户名','密码','登录']:
    click(i)
time.sleep(4)
click('作家工具')
click('发表新作')
click('选择类别')
click('其他类型')
click('文章名称')
pg.typewrite('1')
click('管理员')
pg.press('shift')
pg.typewrite('yoonamessi')
click('作者')
pg.typewrite('1')
click('内容简介')
pp.copy('你好')
pg.hotkey('ctrl','v')
click('新作提交')
time.sleep(4)
click('新建分卷')
click('新增分卷')
pg.typewrite('1')
click('分卷提交')
time.sleep(4)
click('增加章节')
click('章节标题')
pp.copy('你好')
pg.hotkey('ctrl','v')
pg.press('enter')
click('章节内容')
pp.copy('你好')
pg.hotkey('ctrl','v')
click('章节提交')
time.sleep(4)