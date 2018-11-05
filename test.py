IMG_NEED = 200
import PIL.Image
for i in range(16):
    number = str(i + 1)
    img = PIL.Image.open("/home/ars/Документы/Венчурный Акселератор/Ангина/Бактериальная/" + number + ".jpg")
    #коэффициент масштабирования изображения
    h, w = img.size
    x = (h - 200) / 2
    y = (w - 200) / 2
    area = (x, y, h - x, w - y)
    cropped_img = img.crop(area)

    cropped_img.save("/home/ars/Документы/Венчурный Акселератор/Ангина/Бактериальная New/" + number + ".jpg")