# Micro-Doppler Bird and Drone Classifier

A small Python demo that generates simulated radar signals, turns them into spectrograms, trains a CNN to distinguish birds from drones, converts the model to TensorFlow Lite, and classifies one simulated signal.

> This project uses simulated signals. Its accuracy is not a measure of performance on real radar data.

## Pipeline

1. `src/make_data.py` creates 200 drone and 200 bird signals and saves them in `data/signals.npy` with labels in `data/labels.npy`.
2. `src/make_spectrograms.py` converts each signal into a 64 x 64 image and saves `data/images.npy`.
3. `src/train_model.py` trains the CNN, reports accuracy on a held-out test split, and saves `models/drone_bird_model.keras`.
4. `src/convert_tflite.py` converts the trained model and saves `models/drone_bird_model.tflite`.
5. `src/predict.py` creates a simulated drone signal, makes its spectrogram, and prints the predicted class and confidence.

## Requirements

- Python 3.10 or newer
- Packages listed in `requirements.txt`

## Run the whole pipeline

Open PowerShell in this project folder. Create and activate a virtual environment, then install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run all five steps in order:

```powershell
python main.py
```

The project includes a convenience script too:

```powershell
.\run.ps1
```

`run.ps1` uses the project's `.venv` Python. Install dependencies into that environment first if needed:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run an individual step

Run these from the project folder, in order. The later steps need files created by earlier ones.

```powershell
python -m src.make_data
python -m src.make_spectrograms
python -m src.train_model
python -m src.convert_tflite
python -m src.predict
```

## Files created by running

- `data/signals.npy`: simulated radar signals
- `data/labels.npy`: labels (`0` = bird, `1` = drone)
- `data/images.npy`: spectrogram images used for training
- `models/drone_bird_model.keras`: trained Keras model
- `models/drone_bird_model.tflite`: TensorFlow Lite model used for prediction

These are generated outputs and can be recreated by running `python main.py`.

## Browse data and model contents on GitHub

The full `.npy`, `.keras`, and `.tflite` files are stored as binary artifacts and can be downloaded, but GitHub does not display their internal contents as readable text. Open [`data/DATA_README.md`](data/DATA_README.md) for file details and CSV previews, including all labels, one signal, and one spectrogram. Open [`models/MODEL_README.md`](models/MODEL_README.md) and [`models/model_architecture.json`](models/model_architecture.json) to inspect the model description. The source pipeline is in [`src/`](src/).
