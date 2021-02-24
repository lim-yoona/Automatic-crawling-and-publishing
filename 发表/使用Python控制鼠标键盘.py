"""
尝试通过Python控制鼠标键盘，模拟人的行为来登录网站、发表文章
"""
import pyautogui as pg
w,h=pg.size() #获取屏幕尺寸
X,Y=pg.position()#返回当前鼠标位置
print(w,h)
print(X,Y)
pg.PAUSE=1.5#每个函数执行后停顿1.5秒
pg.FAILSAFE=True #鼠标移动到左上角触发异常，程序停止
pg.moveTo(w/2,h/2,duration=0.5)#移动到指定位置
X,Y=pg.position()
print(X,Y)
"""
测试完毕
"""