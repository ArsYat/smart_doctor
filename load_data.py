import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion

IMG_SIZE = 200
OUTPUT_CLASSES = 3
LR = 1e-3

TRAIN_DIR = 'data/trainBV'
TRAIN_FIL = 'data/train_data_{}_{}.npy'.format(IMG_SIZE, OUTPUT_CLASSES)
TEST_DIR = 'data/testBV'
TEST_FIL = 'data/test_data_{}_{}.npy'.format(IMG_SIZE, OUTPUT_CLASSES)

MODEL_NAME = 'Models/virandbac-{}-{}-{}-{}.model'.format(IMG_SIZE, OUTPUT_CLASSES, LR, '2conv-basic')


def label_img(img):
    word_label = img[0:3]
    # conversion to one-hot array
    if word_label == 'Vir': return [1,0,0]
    elif word_label == 'Bac': return [0,1,0]
    elif word_label == 'Nor': return [0,0,1]


def create_train_data(train_dir, save_file):
    train_data = []
    for img in tqdm(os.listdir(train_dir)):
        label = label_img(img)
        path = os.path.join(train_dir, img)
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        train_data.append([np.array(img),np.array(label)])
    shuffle(train_data)
    np.save(save_file, train_data)
    return train_data


def process_test_data():
    test_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR, img)
        img_num = img.split('.')[0]
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        test_data.append([np.array(img), img_num])

    shuffle(test_data)
    np.save('data/test_data.npy', test_data)
    return test_data


def load_data(load_file):
    return np.load(load_file)
