# -*- coding: utf-8 -*-
"""Task_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16uxV50DgkScuOTNcn4ZqdAU0_BnF85jL
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

model = keras.models.load_model('/content/task2.h5')

class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

img = keras.preprocessing.image.load_img(
    '/content/1.jpg', target_size=(180, 180)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

