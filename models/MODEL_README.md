# Model files

- `drone_bird_model.keras`: complete trained Keras model, including learned weights.
- `drone_bird_model.tflite`: TensorFlow Lite binary used by the prediction step.
- `model_architecture.json`: readable JSON description of the Keras model layers and configuration.

GitHub can display the JSON architecture and this document. The learned numeric weights are stored in the binary model files and should be loaded with Keras or TensorFlow Lite; raw weight numbers are not a useful human-readable model document.

Expected input: one 64 x 64 grayscale spectrogram, shaped `(1, 64, 64, 1)`. The single sigmoid output is the model score for class 1 (drone); values below 0.5 are labeled bird by the demo.
