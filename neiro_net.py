import numpy as np

from load_data import IMG_SIZE, MODEL_NAME, load_data, create_train_data, TRAIN_DIR, TRAIN_FIL

from load_model import load_model

model = load_model()

train_data = create_train_data(TRAIN_DIR, TRAIN_FIL)
# train_data = load_data(TRAIN_FIL)

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=3, validation_set=({'input': test_x}, {'targets': test_y}),
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)