import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion

TRAIN_DIR = 'data/trainBV'
TEST_DIR = 'data/testBV'
IMG_SIZE = 50
LR = 1e-3

MODEL_NAME = 'Models/virandbac-{}-{}.model'.format(LR, '2conv-basic') # just so we remember which saved model is which, sizes must match

def label_img(img):
    word_label = img[0:3]
    # conversion to one-hot array
    if word_label == 'Vir': return [1,0]
    elif word_label == 'Bac': return [0,1]

def create_train_data(train_dir, save_file):
    training_data = []
    for img in tqdm(os.listdir(train_dir)):
        label = label_img(img)
        path = os.path.join(train_dir, img)
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save(save_file, training_data)
    return training_data


def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR, img)
        img_num = img.split('.')[0]
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        testing_data.append([np.array(img), img_num])

    shuffle(testing_data)
    np.save('data/test_data.npy', testing_data)
    return testing_data

def load_data(load_file):
    return np.load(load_file)
