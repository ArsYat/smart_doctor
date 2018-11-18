import cv2
from PIL import Image, ImageDraw

IMG_SIZE2 = 200


def newsize(img):
    h, w, _ = img.shape
    scale = IMG_SIZE2 / max(h, w)
    img.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS)

for i in range(16):
    number = str(i + 1)
    img = cv2.imread('/home/ars/Документы/Венчурный Акселератор/Ангина/Нормальная/' + number + '.jpg')

    img = newsize(img)
    cv2.imwrite('/home/ars/Документы/Венчурный Акселератор/Ангина/Normal Size Nor/' + number + '.jpg', img)