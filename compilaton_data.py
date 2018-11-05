import cv2
from PIL import Image, ImageDraw

IMG_SIZE = 200
for i in range(16):
    number = str(i + 1)
    img = cv2.imread('/home/ars/Документы/Венчурный Акселератор/Ангина/Вирусная/' + number + '.jpg')

    def size(img_need):
        h, w = img_need.size
        scale = 200 / max(h, w)
        img_need.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS)

    img = size(img)
    cv2.imwrite('/home/ars/Документы/Венчурный Акселератор/Ангина/Normal Size V/' + number + '.jpg', img)