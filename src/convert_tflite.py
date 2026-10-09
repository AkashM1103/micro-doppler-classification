# Step 4: Convert the trained model to TensorFlow Lite.
import tensorflow as tf
from tensorflow import keras

def convert_tflite():
    model = keras.models.load_model("models/drone_bird_model.keras")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    lite_model = converter.convert()
    with open("models/drone_bird_model.tflite", "wb") as model_file:
        model_file.write(lite_model)
    print("Step 4 done: TFLite model saved ({:.1f} KB)".format(len(lite_model) / 1024))
