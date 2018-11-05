import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

image = Image.open("/home/ars/Документы/Венчурный Акселератор/Тест.jpg") #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.
factor = int(input('factor:'))
for i in range(width):
    for j in range(height):
        rand = random.randint(-factor, factor)
        a = pix[i, j][0] + rand
        b = pix[i, j][1] + rand
        c = pix[i, j][2] + rand
        if (a < 0):
            a = 0
        if (b < 0):
            b = 0
        if (c < 0):
            c = 0
        if (a > 255):
            a = 255
        if (b > 255):
            b = 255
        if (c > 255):
            c = 255
        draw.point((i, j), (a, b, c))
image.save("/home/ars/Документы/Венчурный Акселератор/Результат4.jpg", "JPEG")
del draw