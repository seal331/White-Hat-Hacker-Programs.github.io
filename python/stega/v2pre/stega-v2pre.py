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

def stega_decrypt():
    print("This feature had not been implemented yet! That's why it's a beta.")

#def DetectMode():
#    path = input('Введите путь к файлу серийного ключа ')
#    serialfile = open(path,"r")
#    serialnum = serialfile.read()
#    serialfile.close()
#    test1 = int(serialnum) + 1
#    test2 = test1 - 556
#    test3 = test2 + 1
#    test4 = test3 - 13
#    test5 = test4 / 4
#    test6 = test5 * 2
#    
#    if test6 == 546.0:
#        print('Валидный серийный номер идентифицирован. Вхожу в режим стенографии.')
#        stega_encrypt()
#    else:
#        print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
#        openTulenta()

# DetectMode()

def shell():
    print('*****************************************************************')
    print('УНИВЕРСАЛЬНАЯ ОБОЛОЧКА SEAL SOLUTIONS, ЛИЦЕНЗИРОВАНА ENCRYPT INC.')
    print('     АДАПТИРОВАНА ДЛЯ СТЕНОГРАФИИ КОМПАНИЕЙ ENCRYPT INC, 2020    ')
    print('                       SEAL SOLUTIONS, 2020                      ')
    print('*****************************************************************')
    print(' ')
    print('1. Шифровка по методу стенографии')
    print('2. Дешифровка по методу стенографии')
    print('3. Открыть Тюленту')
    print('Введите число от 1 до 3 для выбора.')
    whattoopen = int(input())
    if whattoopen == 1:
        stega_encrypt()
    elif whattoopen == 2:
        stega_decrypt()
    elif whattoopen == 3:
        openTulenta()
    else:
        print('Невалидный выбор.')

def Serialization():
    path = input('Введите путь к файлу серийного ключа ')
    serialfile = open(path,"r")
    signature = serialfile.read(7)
    number = serialfile.read()
    serialfile.close()
    if signature == 'SIGNENC':
        test1 = int(number) - 5
        test2 = test1 * 4
        test3 = test2 + 314
        test4 = test3 * 99
        test5 = test4 + 4
        test6 = test5 / 3144
        test7 = test6 + 2
        if test7 == 1252154220.6215012:
            print('Серийный ключ для режима шифровки по методу стенографии обнаружен. Включаю соответствующую функцию.')
            stega_encrypt()
        else:
            print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
            openTulenta()
    elif signature == 'SIGNDEC':
        test1 = int(number) + 8
        test2 = test1 - 13
        test3 = test2 * 0.2
        test4 = test3 + 14
        test5 = test4 - 122
        test6 = test5 + 1143
        test7 = test6 * 4.2
        if test7 == 3771894614.0400004:
            print('Серийный ключ для режима дешифровки по методу стенографии обнаружен. Включаю соответствующую функцию.')
            stega_decrypt()
        else:
            print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
            openTulenta()
    elif signature == 'SIGNUNV':
        test1 = int(number) - 0.2
        test2 = test1 + 1.8
        test3 = test2 * 0.2
        test4 = test3 * 34.14
        test5 = test4 - 9999999.1
        test6 = test5 + 14
        test7 = test6 - 145.9
        if test7 == 11357949889.2528:
            print('Универсальный серийный ключ обнаружен. Запускаю универсальную оболочку.')
            shell()
        else:
            print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
            openTulenta()
    else:
            print('Серийный номер неидентифицирован или невалиден. Вхожу в режим открытия Тюленты.')
            openTulenta()

Serialization()
