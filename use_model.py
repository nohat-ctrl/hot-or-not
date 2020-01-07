import cv2
import tensorflow as tf
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def prepare(filepath):
    IMG_SIZE = 200  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

images = []
model = tf.keras.models.load_model("beauty_checker.model")

path = "utilities/manual_testing_cropped"
for img in os.listdir(path):
    image = "utilities/manual_testing_cropped/"+img
    prediction = model.predict_classes(prepare(image))
    print(img,prediction)
    image1 = mpimg.imread(image)
    plt.imshow(image1)
    plt.show()

