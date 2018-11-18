from load_data import IMG_SIZE
import numpy as np
from load_model import load_model

def answer(img):
    labels = ['vir', 'bac', 'nor']

    model = load_model()

    img = np.array(img)

    reshaped_data = img.reshape(IMG_SIZE, IMG_SIZE, 1)

    model_out = model.predict([reshaped_data])[0] # ответ нейронной сети

    pred = np.argmax(model_out)

    print(labels[pred], model_out[pred])



