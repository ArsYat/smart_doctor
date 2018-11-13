import matplotlib.pyplot as plt
import numpy as np
from load_data import IMG_SIZE, create_train_data, load_data, TEST_DIR, TEST_FIL
from load_model import load_model

labels = ['vir', 'bac', 'nor']

model = load_model()

test_data = create_train_data(TEST_DIR, TEST_FIL)
# test_data = load_data(TEST_FIL)

fig = plt.figure()

for num, data in enumerate(test_data[100:112]):

    img_data = data[0]

    y = fig.add_subplot(3, 4, num + 1)
    orig = img_data

    model_out = model.predict([img_data.reshape(IMG_SIZE, IMG_SIZE, 1)])[0]

    pred = np.argmax(model_out)
    fact = np.argmax(data[1])

    y.imshow(orig, cmap='gray')
    plt.title('Pred:{} Fact:{}'.format(labels[pred], labels[fact]))
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)

plt.show()
