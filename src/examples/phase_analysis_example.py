"""
Example: Phase Derivative Analysis on Sample Data
This demonstrates the conceptual framework of the Helic Axis Model.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: a simple sine wave with a phase shift (simulating solar activity)
time = np.linspace(0, 10, 1000)
frequency = 1.0
phase_shift = np.pi / 4  # Represents a "event"

signal_before = np.sin(2 * np.pi * frequency * time)
signal_after = np.sin(2 * np.pi * frequency * time + phase_shift)

# Calculate a simple derivative (proxy for phase change rate)
derivative = np.diff(signal_after) / np.diff(time)

# Find the point of maximum change (the "event")
max_change_index = np.argmax(np.abs(derivative))

print(f"[EXAMPLE] Maximum phase derivative detected at time: {time[max_change_index]:.2f}")
print("[EXAMPLE] This simulates the detection of a predictive signature.")

# Plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title("Sample Signal with Phase Shift (Simulated Data)")
plt.plot(time, signal_before, label='Normal Baseline')
plt.plot(time, signal_after, label='With Phase Shift Event')
plt.axvline(x=time[max_change_index], color='r', linestyle='--', label='Predicted Event')
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Phase Derivative (Rate of Change)")
plt.plot(time[:-1], np.abs(derivative))
plt.axvline(x=time[max_change_index], color='r', linestyle='--')
plt.xlabel("Time")
plt.tight_layout()
plt.savefig('example_phase_analysis.png')
print("[EXAMPLE] Plot saved to 'example_phase_analysis.png'.")
