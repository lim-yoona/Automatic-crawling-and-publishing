import os
novel_list=os.listdir('..\\爬取\\权力的游戏\\正文')
#novel_list.sort(key=lambda x:int(x[:4]))
print(novel_list)
fb=open('..\\爬取\\权力的游戏\\正文'+'\\'+novel_list[0],'r',encoding='utf-8')
str1=fb.read()
print(str1)