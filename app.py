import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input


model = Sequential()

model.add(ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3)))
model.add(GlobalMaxPooling2D())

model.trainable = False

print(model.summary())