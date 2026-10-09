# Step 3: Train a small bird-or-drone classifier.
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras

def train_model():
    images = np.load("data/images.npy")
    labels = np.load("data/labels.npy")
    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42, stratify=labels)
    model = keras.Sequential([
        keras.layers.Input(shape=(64, 64, 1)),
        keras.layers.Conv2D(16, 3, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(32, 3, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(32, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=10, batch_size=16, validation_split=0.1, verbose=2)
    _, accuracy = model.evaluate(x_test, y_test, verbose=0)
    model.save("models/drone_bird_model.keras")
    print("Step 3 done: test accuracy = {:.1%}".format(accuracy))
