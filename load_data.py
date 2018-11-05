import cv2
from PIL import Image

count = 16  # количество картинок для обработки
IMG_SIZE = 1000
IMG_CROP_X = 500
IMG_CROP_Y = 500
for i in range(count):
    number = str(i + 1)
    img = cv2.imread('/home/ars/Документы/Венчурный Акселератор/Ангина/Бактериальная/' + number + '.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    cv2.imwrite('/home/ars/Документы/Венчурный Акселератор/Ангина/Редактированная/' + number + '.jpg', img)

    img = Image.open('/home/ars/Документы/Венчурный Акселератор/Ангина/Редактированная/' + number + '.jpg')

    area = (0, 0, IMG_CROP_X, IMG_CROP_Y)
    cr_img = img.crop(area)

    cr_img.save('/home/ars/Документы/Венчурный Акселератор/Ангина/Редактированная/' + number + '.jpg')

