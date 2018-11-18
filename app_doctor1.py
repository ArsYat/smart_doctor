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

page1 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Фон1.png').convert_alpha()
page2 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Фон2.png').convert_alpha()

def image1():
    screen.blit(page1, (0, 0))
    write(name, 30, 25, 160, 255, 158, 0)
    write(str(age), 30, 150, 160, 255, 158, 0)
    write(str(time), 30, 275, 160, 255, 158, 0)
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
            howMany += 1
            cv2.destroyAllWindows()
    for i in range(0,howNeed):
        if countPhoto[i] == 1:
            path = '/home/ars/Документы/Венчурный Акселератор/Приложение/Снимок'+ str(i) + '.jpg'
            image = pygame.image.load(path).convert_alpha()
            screen.blit(image, (175,110))

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    pygame.display.flip()

    answer(img)
    return img


def click():
    def display_full_name():
        root.destroy()

    root = Tk()
    root.title("Данные пациента")

    name = StringVar()
    age = IntVar()
    time = IntVar()

    name_label = Label(text="Введите ваш пол:")
    age_label = Label(text="Введите ваш возраст:")
    time_label = Label(text="Длительность заболевания(дн):")

    name_label.grid(row=0, column=0, sticky="w")
    age_label.grid(row=1, column=0, sticky="w")
    time_label.grid(row=2, column=0, sticky="w")

    name_entry = Entry(textvariable=name)
    age_entry = Entry(textvariable=age)
    time_entry = Entry(textvariable=time)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    age_entry.grid(row=1, column=1, padx=5, pady=5)
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    message_button = Button(text="Сохранить", command=display_full_name)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    root.mainloop()
    return name.get(), age.get(), time.get()

def write(word,font_c,xText,yText,r,g,b):
    font = pygame.font.Font(None,font_c)
    text = font.render(word, True,[r,g,b])
    textpos = (xText,yText)
    screen.blit(text,textpos)

screen.blit(page1, (0, 0))
pygame.display.flip()

name, age, time = click()
running = True
while running:
    if number == 1:
        image1()

    if number == 2:
        image = image2()
    pygame.display.flip()
