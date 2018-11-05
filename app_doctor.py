import pygame
from PIL import Image

pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
image1 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Логотип Мини.jpg').convert_alpha()

ill1 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Иконка1New.png').convert_alpha()
ill2 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Иконка2New.png').convert_alpha()
ill3 = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/Иконка3New.png').convert_alpha()

camera = pygame.image.load('/home/ars/Документы/Венчурный Акселератор/Приложение/КамераNew.png').convert_alpha()

xI = 5
yI = 5
font1 = pygame.font.Font("/home/ars/Документы/Венчурный Акселератор/Приложение/Orbitron.ttf", 65)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 25)


text1 = font1.render("Smart Doctor 2.0", True, [255, 255, 255])
text1pos = (150, 20)

text2 = font2.render("Ваш пол:", True, [255, 158, 0])
text2pos = (25, 125)

text3 = font2.render("Возраст:", True, [255, 158, 0])
text3pos = (150, 125)

text4 = font2.render("Длительность болезни:", True, [255, 158, 0])
text4pos = (275, 125)

text5 = font2.render("Симптомы:", True, [255, 158, 0])
text5pos = (550, 125)

article1 = font3.render("Введите свои данные", True, [255, 158, 0])
article2 = font3.render("и симптомы для точной", True, [255, 158, 0])
article3 = font3.render("постановки диагноза.", True, [255, 158, 0])

article4 = font3.render("Сфотографируйте", True, [255, 158, 0])
article5 = font3.render("беспокоющую область", True, [255, 158, 0])
article6 = font3.render("тела и выберите самые", True, [255, 158, 0])
article7 = font3.render("скачественные снимки.", True, [255, 158, 0])

article8 = font3.render("Получите результат", True, [255, 158, 0])
article9 = font3.render("анализа и действуйте", True, [255, 158, 0])
article10 = font3.render("по его указаниям.", True, [255, 158, 0])

xCircle = 740
yCircle = 540
rCircle = 52

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 158, 0), ((0, 0), (size[0], 100)))
    screen.blit(image1, (xI, yI))

    screen.blit(text1, text1pos)
    screen.blit(text2, text2pos)
    screen.blit(text3, text3pos)
    screen.blit(text4, text4pos)
    screen.blit(text5, text5pos)

    for i in range(3):
        number = str(i + 1)
        x = 25 + 250 * i
        pygame.draw.circle(screen, (255, 158, 0), (x, 400), 15)
        count = font2.render(number, True, [255,255,255])
        countpos = (x-5, 392.5)
        screen.blit(count, countpos)
    article1pos = (45,392.5)
    article2pos = (45,410)
    article3pos = (45,427.5)

    screen.blit(article1,article1pos)
    screen.blit(article2,article2pos)
    screen.blit(article3,article3pos)

    article4pos = (295, 392.5)
    article5pos = (295, 410)
    article6pos = (295, 427.5)
    article7pos = (295, 445)

    screen.blit(article4,article4pos)
    screen.blit(article5,article5pos)
    screen.blit(article6,article6pos)
    screen.blit(article7,article7pos)

    article8pos = (545, 392.5)
    article9pos = (545, 410)
    article10pos = (545, 427.5)

    screen.blit(article8,article8pos)
    screen.blit(article9,article9pos)
    screen.blit(article10,article10pos)

    screen.blit(ill1, (70, 460))
    screen.blit(ill2, (330, 470))
    screen.blit(ill3, (570, 460))

    pygame.draw.circle(screen, (255, 158, 0), (xCircle, yCircle), rCircle)

    screen.blit(camera, (690, 490))

    pygame.display.flip()
pygame.quit()
