import pyautogui as pg
import time
dict={}
dict['用户名']=[446,311]
dict['密码']=[435,340]
dict['登录']=[393,400]
time.sleep(5)
for i in ['用户名','密码','登录']:
    pg.click(dict[i][0],dict[i][1])
