# Step 2: Turn radar signals into small spectrogram images.
import numpy as np
from scipy.ndimage import zoom
from scipy.signal import spectrogram

def signal_to_image(signal):
    _, _, power = spectrogram(signal, fs=1000, nperseg=128, noverlap=96, return_onesided=False)
    power = np.fft.fftshift(power, axes=0)
    power = 10 * np.log10(power + 1e-10)
    value_range = power.max() - power.min()
    if value_range > 0:
        power = (power - power.min()) / value_range
    return zoom(power, (64 / power.shape[0], 64 / power.shape[1]))

def make_spectrograms():
    signals = np.load("data/signals.npy")
    images = [signal_to_image(signal) for signal in signals]
    images = np.array(images, dtype=np.float32)[..., np.newaxis]
    np.save("data/images.npy", images)
    print("Step 2 done: spectrogram shape", images.shape)
