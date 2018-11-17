import random

import matplotlib.pyplot as plt
import numpy as np
from load_data import IMG_SIZE, create_train_data, load_data, TEST_DIR, TEST_FIL, TRAIN_DIR, TRAIN_FIL
from load_model import load_model

labels = ['vir', 'bac', 'nor']

model = load_model()

test_data = create_train_data(TEST_DIR, TEST_FIL)
# test_data = create_train_data(TRAIN_DIR, TRAIN_FIL)
# test_data = load_data(TEST_FIL)

fig = plt.figure()

pos = int(random.random()*(3000-12))

# for num in range(0,12):
#     data = test_data[num+pos]

for num, data in enumerate(test_data[pos:pos+12]):

    img_data = data[0]

    fact = np.argmax(data[1])

    y = fig.add_subplot(3, 4, num + 1)

    reshaped_data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)

    model_out = model.predict([reshaped_data])[0]

    pred = np.argmax(model_out)

    y.imshow(img_data, cmap='gray')
    plt.title('Pred:{}({}%) Fact:{}'.format(labels[pred], "%.3f" % model_out[pred], labels[fact]))
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)

plt.show()
