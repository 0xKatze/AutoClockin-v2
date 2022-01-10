#載入requests套件
import requests
#需要載入os套件，可處理文件和目錄
import os
#創建目錄
os.makedirs('./img/',exist_ok=True)
url='https://course.fcu.edu.tw/validateCode.aspx'
r=requests.get(url)
for index in range(1,100):
    r=requests.get(url)
    with open('./img/'+str(index)+'.jpg','wb') as f:
    #將圖片下載下來
        f.write(r.content)
        f.close()