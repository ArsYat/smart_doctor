from PIL import Image, ImageDraw
import random
import cv2
import numpy as np

IMG_SIZE = 200

# def size(img_need):
   # img_need = img_need.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
   # return img_need

def brightness(img_need):
    draw = ImageDraw.Draw(img)  # Создаем инструмент для рисования.
    for i in range(IMG_SIZE):
        for j in range(IMG_SIZE):
            a = round(pix[i, j][0] * brightness_f)
            b = round(pix[i, j][1] * brightness_f)
            c = round(pix[i, j][2] * brightness_f)
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
    return img_need

def perspective(img_need):
    rows, cols, ch = img_need.shape

    pts1 = np.float32([[0, 0], [200,0], [0, 200], [200, 200]])
    pts2 = np.float32([[point1, point2], [point3, point4], [point5, point6], [point7, point8]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img_need, M, (IMG_SIZE, IMG_SIZE))
    return dst

def mirror(img):
    img = cv2.flip(img, 1)
    return img

number1 = 1
number2 = 1
while number2 <= 2000:
    brightness_f = (random.random() * 0.6 + 0.7)

    point1 = random.randint(-50, 0)
    point2 = random.randint(-50, 0)

    point3 = random.randint(200, 250)
    point4 = random.randint(-50, 0)

    point5 = random.randint(-50, 0)
    point6 = random.randint(200, 250)

    point7 = random.randint(200, 250)
    point8 = random.randint(200, 250)

    img = Image.open('/home/ars/Документы/Венчурный Акселератор/Ангина/Normal Size V/' + str(number1) + '.jpg')
    # img = size(img)

    pix = img.load() #Выгружаем значения пикселей.
    width = img.size[0] #Определяем ширину.
    height = img.size[1] #Определяем высоту.

    img = brightness(img)
    img.save("/home/ars/Документы/Венчурный Акселератор/Ангина/Вирусная Train/Vir" + str(number2) + ".jpg", "JPEG")

    img = cv2.imread('/home/ars/Документы/Венчурный Акселератор/Ангина/Вирусная Train/Vir' + str(number2) + '.jpg')
    number2 += 1
    img = perspective(img)
    img = mirror(img)
    cv2.imwrite('/home/ars/Документы/Венчурный Акселератор/Ангина/Вирусная Train/Vir' + str(number2) + '.jpg',img)
    number2 += 1
    number1 += 1
    if number1 == 16:
        number1 = 1
