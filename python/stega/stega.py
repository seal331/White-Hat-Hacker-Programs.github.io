from PIL import Image, ImageDraw
from random import randint
import webbrowser

def openTulenta():
    webbrowser.open('vk.com/tulenta')
def stega_encrypt():
    text = input('Введите текст латиницей ')
    keys = []
    img = Image.open(input('Введите название картинки '))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('keys.txt', 'w')

    for elem in ([ord(elem) for elem in text]):
        key = (randint(1,width-10), randint(1,height-10))
        r,g, b = pix[key][:3]
        draw.point(key, (r,elem , b))
        f.write(str(key)+'\n')


    img.save("newimage.png", "PNG")
    f.close()

def DetectMode():
    path = input('Введите путь к файлу серийного ключа ')
    serialfile = open(path,"r")
    serialnum = serialfile.read()
    serialfile.close()
    test1 = int(serialnum) + 1
    test2 = test1 - 556
    test3 = test2 + 1
    test4 = test3 - 13
    test5 = test4 / 4
    test6 = test5 * 2
    
    if test6 == 546.0:
        print('Валидный серийный номер идентифицирован. Вхожу в режим стенографии.')
        stega_encrypt()
    else:
        print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
        openTulenta()

DetectMode()

