"""
--------------------------------------------------------------------------
test_filter.py
--------------------------------------------------------------------------
Project : NeuroSwitch - EEG Light Switch (EDES301 Project 01)
Author  : Sunny Yu
Date    : 2026-11-16

Description:
    Tests the SignalFilter class with a simulated signal
    (800 DC offset + 10/20/60 Hz sines + noise). Checks that only
    the 10 Hz component remains and that block-by-block filtering
    matches filtering the whole signal at once.

Usage:
    python test_filter.py

--------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_filter import SignalFilter

fs = 250  # Sampling frequency
t = np.arange(2500) / fs  # Time vector for 10 seconds

simulated_signal = (800 + 10 * np.sin(2 * np.pi * 10 * t) +
    np.sin(2 * np.pi * 20 * t) + 
    np.sin(2 * np.pi * 60 * t) + 
    0.5 * np.random.randn(len(t)))

filt = SignalFilter(sampling_rate=fs, notch_freq=60, notch_q=30, low=8, high=12, order=4)
filter_signal = filt.process(simulated_signal)



filt2 = SignalFilter(sampling_rate=fs, notch_freq=60, notch_q=30, low=8, high=12, order=4)
chunks = []
for i in range(0, len(simulated_signal), 63):
    chunk = simulated_signal[i:i+63]
    filtered_chunk = filt2.process(chunk)
    chunks.append(filtered_chunk)
filter_signal_block = np.concatenate(chunks)
print(np.allclose(filter_signal_block, filter_signal))



#plot result
plt.figure(figsize=(12, 6))

# --- Top: raw simulated signal ---
plt.subplot(2, 1, 1)
plt.plot(t, simulated_signal, label='Simulated Signal', color='blue')
plt.title('Simulated EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 2)        
plt.legend()             

# --- Bottom: filtered signal ---
plt.subplot(2, 1, 2)
plt.plot(t, filter_signal, label='Filtered Signal', color='orange')
plt.title('Filtered EEG Signal (Notch + Bandpass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 2)  
plt.legend()    

plt.tight_layout()
plt.show()



