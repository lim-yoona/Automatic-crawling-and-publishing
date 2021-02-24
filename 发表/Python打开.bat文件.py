import pyautogui as pg
pg.PAUSE=0.25#每个函数执行后停顿1.5秒
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