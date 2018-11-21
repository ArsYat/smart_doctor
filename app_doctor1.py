import pygame
# from show import ___ ; ___() - вызов
from anwser_data import answer

from tkinter import *
import cv2

from load_data import IMG_SIZE

pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
number = 1
diagnosis = ""

page1 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Фон1.png').convert_alpha()
page2 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Фон2.png').convert_alpha()
page3 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Фон3.png').convert_alpha()

def image1():
    screen.blit(page1, (0, 0))
    for i in range(len(symptoms)):
        write(str(symptoms[i]), 30, 20 + i * 200, 160, 255, 158, 0)
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            mouseX, mouseY = i.pos
            if mouseX >= 692 and mouseX <= 791 and mouseY >= 490 and mouseY <= 591:
                global number
                number = 2

needPhoto = 0
countPhoto = [0,0,0,0,0]
howMany = 0
howNeed = 1
coeff = 1.4

def image2():
    screen.blit(page2, (0, 0))
    cap = cv2.VideoCapture(1)
    global needPhoto, howMany, countPhoto, coeff
    while cap.isOpened() and needPhoto < howNeed:
        _ , img = cap.read()
        cv2.imshow('Your Photo', img)
        if cv2.waitKey(1) == ord('w'):
            needPhoto += 1
            countPhoto[howMany] = 1
            xSize = round(640 / coeff)
            ySize = round(480 / coeff)
            img = cv2.resize(img, (xSize,ySize))  #427, 320 - необходимый сжатый размер изображения
            cv2.imwrite("/home/ars/Документы/Венчурный Акселератор/Приложение/Снимок" + str(howMany)+ ".jpg",img)
            # howMany += 1 - предназначено для сохранения нескольких фото, на данный момент не нужно.
            cv2.destroyAllWindows()
    for i in range(0,howNeed):
        if countPhoto[i] == 1:
            path = '/home/ars/Документы/Венчурный Акселератор/Приложение/Снимок'+ str(i) + '.jpg'
            write("Изображение сохранено", 30, 270, 555, 10, 136, 19)
            image = pygame.image.load(path).convert_alpha()
            screen.blit(image, (175,110))

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    pygame.display.flip()

    for j in pygame.event.get():
        if j.type == pygame.MOUSEBUTTONDOWN and j.button == 1:
            mouseX, mouseY = j.pos
            if mouseX >= 0 and mouseX <= 150 and mouseY >= 500 and mouseY <= 600:
                needPhoto = 0
            if mouseX >= 650 and mouseX <= 800 and mouseY >= 500 and mouseY <= 600:
                global diagnosis, number
                number = 3
                diagnosis = answer(img)
                symptoms.append(diagnosis)
    return img

def probability():
    result = 0
    if diagnosis == "nor":
        result -= 2
    elif diagnosis == "bac" or diagnosis == "vir":
        result += 2

    if temp >= 38:
        result += 1

    if age <= 14:
        result += 1
    elif age > 43:
        result -= 1

    if time >= 4:
        result += 1
    return result

needProbability = True
to_print = 0

def image3(img):
    global diagnosis, needProbability
    tips = ""
    screen.blit(page3, (0, 0))
    if needProbability:
        global to_print
        to_print = probability()
        needProbability = False
        print(to_print)
    if to_print > 2:
        write("Вам рекомендуется обратиться к врачу", 20, 15, 330, 0, 0, 0)
    else:
        write("Вы здоровы!", 20, 15, 330, 0, 0, 0)
    write(tips,20,15,360,0,0,0)
    for j in range(len(symptoms)):
        write(str(symptoms[j]), 30, 200, 150 + j * 30, 0, 0, 0)
    screen.blit(img, (300, 125))

    for q in pygame.event.get():
        if q.type == pygame.MOUSEBUTTONDOWN and q.button == 1:
            mouseX, mouseY = q.pos
            if mouseX >= 650 and mouseX <= 800 and mouseY >= 540 and mouseY <= 600:
                global number, temp, age, time, needPhoto, howMany, symptoms
                needProbability = True
                to_print = 0
                temp, age, time = click()
                symptoms = [temp, age, time]
                needPhoto = 0
                howMany = 0
                number = 1

def click():
    def display_full_name():
        root.destroy()

    root = Tk()
    root.title("Данные пациента")

    temp = IntVar()
    age = IntVar()
    time = IntVar()

    temp_label = Label(text="Ваша температура:")
    age_label = Label(text="Введите ваш возраст:")
    time_label = Label(text="Длительность заболевания(дн):")

    temp_label.grid(row=0, column=0, sticky="w")
    age_label.grid(row=1, column=0, sticky="w")
    time_label.grid(row=2, column=0, sticky="w")

    temp_entry = Entry(textvariable=temp)
    age_entry = Entry(textvariable=age)
    time_entry = Entry(textvariable=time)

    temp_entry.grid(row=0, column=1, padx=5, pady=5)
    age_entry.grid(row=1, column=1, padx=5, pady=5)
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    message_button = Button(text="Сохранить", command=display_full_name)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    root.mainloop()
    return temp.get(), age.get(), time.get()

def write(word,font_c,xText,yText,r,g,b):
    font = pygame.font.Font(None,font_c)
    text = font.render(word, True,[r,g,b])
    textpos = (xText,yText)
    screen.blit(text,textpos)

screen.blit(page1, (0, 0))
pygame.display.flip()

temp, age, time = click()
symptoms = [temp, age, time]
running = True
while running:
    if number == 1:
        image1()

    if number == 2:
        image = image2()
    if number == 3:
        img = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Снимок0.jpg').convert_alpha()
        image3(img)
    pygame.display.flip()
