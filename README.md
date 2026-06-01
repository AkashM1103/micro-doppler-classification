# 🎯 Micro-Doppler-Based Target Classification

A deep learning prototype for classifying targets using micro-Doppler radar signatures. Built using CNN on NVIDIA Jetson with NumPy-based signal preprocessing.

---

## 📌 Overview

Radar systems emit signals that bounce off moving objects. When parts of a target (like rotating blades or walking limbs) move at different speeds, they create **micro-Doppler shifts** — unique frequency patterns that act like a "fingerprint" for each target type.

This project:
- Studies and visualizes micro-Doppler signatures
- Preprocesses raw radar signals into spectrograms
- Classifies targets using a Convolutional Neural Network (CNN)

---

## 🧠 How It Works

```
Raw Radar Signal
      ↓
Signal Preprocessing (FFT, STFT)
      ↓
Spectrogram Generation (micro-Doppler signature)
      ↓
CNN Model
      ↓
Target Classification (Human / Vehicle / Drone / etc.)
```

---

## 🗂️ Project Structure

```
micro-doppler-classification/
│
├── data/
│   ├── raw/                  # Raw radar signal files
│   └── processed/            # Preprocessed spectrograms
│
├── src/
│   ├── preprocess.py         # Signal preprocessing & spectrogram generation
│   ├── model.py              # CNN model architecture
│   ├── train.py              # Training script
│   └── predict.py            # Inference / prediction script
│
├── notebooks/
│   └── exploration.ipynb     # Data exploration & visualization
│
├── models/
│   └── cnn_model.h5          # Saved trained model (after training)
│
├── results/
│   └── sample_spectrogram.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| NumPy | Signal processing & array operations |
| SciPy | FFT / STFT computations |
| TensorFlow / Keras | CNN model building & training |
| Matplotlib | Spectrogram visualization |
| NVIDIA Jetson Nano | Edge deployment hardware |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AkashM1103/micro-doppler-classification.git
cd micro-doppler-classification
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Preprocess the Data
```bash
python src/preprocess.py
```

### 4. Train the Model
```bash
python src/train.py
```

### 5. Run Prediction
```bash
python src/predict.py --input data/processed/sample.npy
```

---

## 🔬 CNN Architecture

```
Input (Spectrogram Image: 128x128x1)
    → Conv2D(32, 3x3) + ReLU + MaxPooling
    → Conv2D(64, 3x3) + ReLU + MaxPooling
    → Conv2D(128, 3x3) + ReLU + MaxPooling
    → Flatten
    → Dense(256) + Dropout(0.5)
    → Dense(n_classes) + Softmax
```

---

## 📊 Sample Result

> Spectrogram of a walking human vs. a rotating drone blade shows distinctly different micro-Doppler signatures, enabling accurate classification.

---

## 📁 Dataset

This prototype uses simulated micro-Doppler data generated via signal simulation scripts. For real-world datasets, refer to:
- [MSTAR Dataset](https://www.sdms.afrl.af.mil/index.php?collection=mstar)
- [DJI Drone Radar Datasets (public research)]

---

## 🏆 Achievements

- Finalist — **Idea for Life 2025 Innovation Program** (National Level)
- Participant — **Smart India Hackathon 2025**

---

## 👤 Author

**Akash M**  
B.E Computer Science & Engineering, Karpagam Academy of Higher Education  
📧 akashmurugesan1132006@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/akashm11) | [GitHub](https://github.com/AkashM1103)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
