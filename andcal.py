import os
from tkinter import *
import time


device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()

print(device)


print("Waiting for connection ...")

connect = os.popen("adb connect " + device ).read()

print(connect)
#os.system("adb shell input tap 340 1030 340 650 100")
#os.system("adb shell input keyevent 4")   
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.t1=Entry(bd=3)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(win, text='call', command=self.add)
        self.b2=Button(win, text='end call', command=self.endcall)
        self.b1.place(x=100, y=150)
        self.b2.place(x=150, y=150)
    def add(self):
        num1=int(self.t1.get())
        print("calling")
        os.system("adb shell am start -a android.intent.action.CALL -d tel:+91"+str(num1))
          
    def endcall(self):
        os.system("adb shell input keyevent 6")
        print("call ended")
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()