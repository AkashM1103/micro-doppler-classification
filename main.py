# Run the complete bird-versus-drone demo from the project folder.
from src.make_data import make_data
from src.make_spectrograms import make_spectrograms
from src.train_model import train_model
from src.convert_tflite import convert_tflite
from src.predict import predict

make_data()
make_spectrograms()
train_model()
convert_tflite()
predict()
