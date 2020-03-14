from tkinter import *  
from PIL import ImageTk,Image  

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
    if whattoopen == 1:
        yukipic()
    elif whattoopen == 2:
        kroshikpic()
    elif whattoopen == 3:
        zhrunpic()
    else:
        print('Невалидный выбор.')

shell()
