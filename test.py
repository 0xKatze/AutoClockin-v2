from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import urllib.request
import time
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox
from threading import Timer

username = "none"
password = "none"



class Clock():
    def __init__(self, window):
        self.label = Label(window,text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.window = window
        self.update_clock()


    def update_clock(self):
        global nowm
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        nowm = time.localtime(time.time())
        self.window.after(1000, self.update_clock)

def tk():
    global username
    global password
    def enter_clockin():
        username = str(username_entry.get())
        password = str(password_entry.get())
        messagebox.showwarning("注意","請靜候打卡")
        if clockin(username, password) == True:
            messagebox.showinfo("恭喜","打卡成功")
            print(username,password)
        else:
            messagebox.showerror("錯誤","打卡失敗")


    def create_label_image():
        img = PIL.Image.open('fcu.jpg')                    
    # 讀取圖片
        img = img.resize( (img.width , img.height) )   
    # 縮小圖片
        imgTk =  ImageTk.PhotoImage(img)                        
    # 轉換成Tkinter可以用的圖片
        lbl_2 = Label(window, image=imgTk)                   
    # 宣告標籤並且設定圖片
        lbl_2.image = imgTk
        lbl_2.place(x=0, y=0, relwidth=1, relheight=1)
    # CLOCK

    
    
    #
    window = Tk()
    window.title('CLOCK IN')
    window.geometry('600x300')
    window.configure(background='grey')
    create_label_image()
    clock = Clock(window)
    
    header_label = Label(window, text='輸入帳號密碼自動打卡')
    header_label.pack()

    # 以下為 username_frame 群組
    username_frame = Frame(window)
    # 向上對齊父元件
    username_frame.pack(side=TOP)
    username_label = Label(username_frame, text='帳號')
    username_label.pack(side=LEFT)
    username_entry = Entry(username_frame)
    username_entry.pack(side=LEFT)

    # 以下為 password_frame 群組
    password_frame = Frame(window)
    password_frame.pack(side=TOP)
    password_label = Label(password_frame, text='密碼')
    password_label.pack(side=LEFT)
    password_entry = Entry(password_frame)
    password_entry.pack(side=LEFT)

    #result_label = Label(window)
    #result_label.pack()

    calculate_btn = Button(window, text='打卡', command=enter_clockin)
    calculate_btn.pack(side=BOTTOM,ipady=10, ipadx=40,fill=X)

    if nowm.tm_min==38:
        messagebox.showwarning("注意","15分到了 請靜候打卡")
        if clockin(username, password) == True:
            messagebox.showinfo("恭喜","打卡成功")
            print(username,password)
        else:
            messagebox.showerror("錯誤","打卡失敗")
    
    
    window.mainloop()

def validateCode():
    urllib.request.urlretrieve("https://course.fcu.edu.tw/validateCode.aspx",
    "1.png")
    ocr = ddddocr.DdddOcr()
    with open('1.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    
    return res

def clockin(username, password):
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    # 登入
    #UserName = input("Enter User Name:")
    #Password = input("Enter Password:")
    
    
    driver.get('https://signin.fcu.edu.tw/clockin/login.aspx')


    driver.find_element_by_id("LoginLdap_UserName").send_keys(username)
    driver.find_element_by_id("LoginLdap_Password").send_keys(password)
    driver.find_element_by_id("LoginLdap_LoginButton").click()
    driver.find_element_by_id("ButtonClassClockin").click()
    
    vali = validateCode()
    #填入驗證碼
    #driver.find_element_by_id("").send_keys(vali)
    #點擊打卡
    #driver.find_element_by_id("").click
    
    time.sleep(3)
    
    return True

    # 
def main():
    tk()
if __name__ == "__main__":
    main()