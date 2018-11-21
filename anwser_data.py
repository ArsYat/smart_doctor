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
    if model_out[pred] < 0.7:
        neiro_ans = "No"
    else:
        neiro_ans = labels[pred]
    print(labels[pred], model_out[pred])
    return(neiro_ans)


