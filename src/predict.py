# Step 5: Classify one simulated radar signal with the saved TFLite model.
import numpy as np
import tensorflow as tf
from src.make_spectrograms import signal_to_image

def get_signal():
    sample_rate = 1000
    times = np.arange(0, 2, 1 / sample_rate)
    body_speed = 45
    propeller_speed = 120
    phase = 2 * np.pi * body_speed * times + 3 * np.sin(2 * np.pi * propeller_speed * times)
    return np.exp(1j * phase) + 0.3 * np.random.randn(len(times))

def predict():
    interpreter = tf.lite.Interpreter(model_path="models/drone_bird_model.tflite")
    interpreter.allocate_tensors()
    input_info = interpreter.get_input_details()[0]
    output_info = interpreter.get_output_details()[0]
    image = signal_to_image(get_signal())
    image = image[np.newaxis, ..., np.newaxis].astype(np.float32)
    interpreter.set_tensor(input_info["index"], image)
    interpreter.invoke()
    drone_score = float(interpreter.get_tensor(output_info["index"])[0][0])
    if drone_score >= 0.5:
        print("Step 5 result: Drone ({:.1%} confidence)".format(drone_score))
    else:
        print("Step 5 result: Bird ({:.1%} confidence)".format(1 - drone_score))

if __name__ == "__main__":
    predict()
