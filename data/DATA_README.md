# Data files

The `.npy` files contain the complete arrays used by the pipeline. GitHub stores them, but does not display their binary contents as a table. Use the CSV files below for readable examples and labels.

- `signals.npy`: 400 simulated complex radar signals; each has 2,000 samples.
- `labels.npy`: 400 labels; 0 means bird and 1 means drone.
- `images.npy`: 400 grayscale spectrograms, each 64 by 64 pixels.
- `labels.csv`: all sample IDs and readable class names.
- `signal_preview.csv`: real and imaginary parts of the first signal only.
- `spectrogram_preview.csv`: the 64 by 64 values for the first signal's spectrogram.

The previews make representative values viewable on GitHub; the full arrays remain in the `.npy` files.
