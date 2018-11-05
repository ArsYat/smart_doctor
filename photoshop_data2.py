import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

image = Image.open("/home/ars/Документы/Венчурный Акселератор/Тест.jpg") #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.

depth = int(input('depth:'))
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = (a + b + c) // 3
        a = S + depth * 2
        b = S + depth
        c = S
        if (a > 255):
            a = 255
        if (b > 255):
            b = 255
        if (c > 255):
            c = 255
        draw.point((i, j), (a, b, c))
image.save("/home/ars/Документы/Венчурный Акселератор/Результат2.jpg", "JPEG")
del draw