"""
@Time	: 2019-10-28
@Author	: Honeypot
@GitHub	: Alice-py
@e-mail	: 846912416@qq.com
@version	: 1.3
"""
from tkinter.messagebox import *
import tkinter
import tkinter.messagebox
import requests
import RPi.GPIO
import time


class KsglS():
    def __init__(self):
        self.key_ = '001100'
        self.lists = []
        self.isPressSign = False
        self.isPressNum = False
        self.result = None
        self.root = tkinter.Tk()

    def get_key(self):
        url = r'http://honeypot.work:8000/ksglapp/getkey'
        key = requests.get(url)
        self.key_ = key.json()
        print('成功更新智能锁密码，当前密码为:', self.key_)
        upkey = 180000   # 3分钟
        self.root.after(upkey, self.get_key)


    def ksgl_s(self):
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(24, RPi.GPIO.OUT)

    #  *****
    def clear_key(self, sign):
        num = self.result.get()
        self.lists.append(num)
        if sign == 'b':
            a = num[0:-1]
            self.lists.clear()
            self.result.set(a)


    def ksgl_gui(self):
        root = self.root

        root.minsize(480, 420)
        root.title('login')

        self.result = tkinter.StringVar()
        self.result.set('')

        label = tkinter.Label(root, font=('Helvetica', 50), anchor='cente', textvariable=self.result)
        label.place(y=0, width=480, height=90)

        btn7 = tkinter.Button(root, font=('Helvetica', 30), text='7', bd=0.5, command=lambda: self.pressNum('7'))
        btn7.place(x=0, y=100, width=160, height=80)
        btn8 = tkinter.Button(root, font=('Helvetica', 30), text='8', bd=0.5, command=lambda: self.pressNum('8'))
        btn8.place(x=160, y=100, width=160, height=80)
        btn9 = tkinter.Button(root, font=('Helvetica', 30), text='9', bd=0.5, command=lambda: self.pressNum('9'))
        btn9.place(x=320, y=100, width=160, height=80)
        btn4 = tkinter.Button(root, font=('Helvetica', 30), text='4', bd=0.5, command=lambda: self.pressNum('4'))
        btn4.place(x=0, y=180, width=160, height=80)
        btn5 = tkinter.Button(root, font=('Helvetica', 30), text='5', bd=0.5, command=lambda: self.pressNum('5'))
        btn5.place(x=160, y=180, width=160, height=80)
        btn6 = tkinter.Button(root, font=('Helvetica', 30), text='6', bd=0.5, command=lambda: self.pressNum('6'))
        btn6.place(x=320, y=180, width=160, height=80)
        btn1 = tkinter.Button(root, font=('Helvatica', 30), text='1', bd=0.5, command=lambda: self.pressNum('1'))
        btn1.place(x=0, y=260, width=160, height=80)
        btn2 = tkinter.Button(root, font=('Helvatica', 30), text='2', bd=0.5, command=lambda: self.pressNum('2'))
        btn2.place(x=160, y=260, width=160, height=80)
        btn3 = tkinter.Button(root, font=('Helvatica', 30), text='3', bd=0.5, command=lambda: self.pressNum('3'))
        btn3.place(x=320, y=260, width=160, height=80)
        btn0 = tkinter.Button(root, font=('Helvatica', 30), text='0', bd=0.5, command=lambda: self.pressNum('0'))
        btn0.place(x=160, y=340, width=160, height=80)

        btnequ = tkinter.Button(root, font=('Helvatica', 30), text='OK', bd=0.5, command=lambda: self.pressSave('a'))
        btnequ.place(x=0, y=340, width=160, height=80)
        btnback = tkinter.Button(root, font=('Helvatica', 30), text='Del', bd=0.5, command=lambda: self.clear_key('b'))
        btnback.place(x=320, y=340, width=160, height=80)

        self.get_key()

        root.mainloop()

    def pressNum(self, num):
        if self.isPressNum == False:
            pass
        else:
            self.result.set()
            self.isPressNum = False

        oldnum = self.result.get()
        if oldnum == '':
            self.result.set(num)
        else:
            newnum = oldnum + num
            self.result.set(newnum)

    def pressSave(self, sign):
        num = self.result.get()
        self.lists.append(num)
        self.ksgl_s()

        if sign == 'a':
            lennum = len(self.lists[0])
            if lennum == 6 and self.lists[0] == self.key_:
                print('密码正确，当前密码为:' + self.lists[0])
                RPi.GPIO.output(24, True)
                time.sleep(5)
                RPi.GPIO.output(24, False)
                RPi.GPIO.cleanup()
                self.lists.clear()
            else:
                showinfo('error', '密码错误')
                self.lists.clear()

        if sign == 'b':
            a = num[0:-1]
            self.lists.clear()
            self.result.set(a)




   
if __name__ == '__main__':
    ks = KsglS()
    ks.ksgl_gui()
