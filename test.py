from PIL import Image

for i in range(0,1):
    number = str(i + 1)
    image = Image.open("/home/ars/Документы/Венчурный Акселератор/Ангина/Нормальная/" + number + ".jpg")
    def scale_image(original_image,
                    width=None,
                    height=None
                    ):
        w, h = original_image.size

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)
        else:
            raise RuntimeError('Width or height required!')

        original_image.thumbnail(max_size, Image.ANTIALIAS)
        image = original_image

    def cut(img):
        global image
        x, y = img.size
        xNeed = (x - 200) / 2
        yNeed = (y - 200) / 2
        area = (xNeed, yNeed, x - xNeed, y - yNeed)
        img = img.crop(area)
        image = img

    if __name__ == '__main__':
        scale_image(original_image = image,
                    width=None,
                    height=500)
        cut(image)
        image.save("/home/ars/Документы/Венчурный Акселератор/Ангина/Normal Size Nor/" + number + ".jpg")