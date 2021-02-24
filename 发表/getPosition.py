import pyautogui as pg
import time
dict={}
while True:
    time.sleep(5)
    x,y=pg.position()
    str1=input('请输入:')
    dict[str1]=[x,y]
    if str1=='#':
        break
print(dict)


