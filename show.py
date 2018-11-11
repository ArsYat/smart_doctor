import matplotlib.pyplot as plt
import numpy as np
from load_data import IMG_SIZE, load_data
from load_model import load_model


model = load_model()

test_data = load_data('data/test_data.npy')

fig = plt.figure()

for num, data in enumerate(test_data[100:112]):
    # cat: [1,0]
    # dog: [0,1]

    img_num = data[1]
    img_data = data[0]

    y = fig.add_subplot(3, 4, num + 1)
    orig = img_data
    data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
    # model_out = model.predict([data])[0]
    model_out = model.predict([data])[0]

    if np.argmax(model_out) == 1:
        str_label = 'vir'
    else:
        str_label = 'bac'

    y.imshow(orig)
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()
