# Step 1: Create simulated radar signals for birds and drones.
import numpy as np

def make_data():
    sample_rate = 1000
    times = np.arange(0, 2, 1 / sample_rate)
    signals = []
    labels = []  # 0 means bird, 1 means drone

    for _ in range(200):
        body_speed = np.random.uniform(20, 80)
        propeller_speed = np.random.uniform(80, 160)
        phase = 2 * np.pi * body_speed * times + 3 * np.sin(2 * np.pi * propeller_speed * times)
        signals.append(np.exp(1j * phase) + 0.3 * np.random.randn(len(times)))
        labels.append(1)

        body_speed = np.random.uniform(20, 80)
        flap_speed = np.random.uniform(3, 10)
        phase = 2 * np.pi * body_speed * times + 15 * np.sin(2 * np.pi * flap_speed * times)
        signals.append(np.exp(1j * phase) + 0.3 * np.random.randn(len(times)))
        labels.append(0)

    np.save("data/signals.npy", np.array(signals))
    np.save("data/labels.npy", np.array(labels))
    print("Step 1 done: saved", len(signals), "signals")
