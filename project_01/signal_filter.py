"""
--------------------------------------------------------------------------
signal_filter.py
--------------------------------------------------------------------------
Project : NeuroSwitch - EEG Light Switch (EDES301 Project 01)
Author  : Sunny Yu
Date    : 2026-11-16

Description:
    SignalFilter class for single-channel EEG on the PocketBeagle.
    Applies a 60 Hz notch filter (powerline noise) followed by an
    8-12 Hz Butterworth band-pass filter (alpha band). Filter state
    (zi) is kept between calls so the signal can be processed in
    real time, one sample or one small block at a time.

Usage:
    filt = SignalFilter()          # defaults: fs=250 Hz, 60 Hz notch, 8-12 Hz
    y = filt.process(x)            # x: single sample or numpy array

Reference:
    Adapted from Chords-Python by Upside Down Labs (ffteeg.DataProcessor)
    https://github.com/upsidedownlabs/Chords-Python
--------------------------------------------------------------------------
"""

import numpy as np
from scipy.signal import butter, iirnotch, lfilter, lfilter_zi


class SignalFilter:
    def __init__(self, sampling_rate=250, notch_freq=60, notch_q=30, low=8, high=12, order=4):
        self.sampling_rate = sampling_rate
        self.notch_freq = notch_freq
        self.notch_q = notch_q
        self.low = low
        self.high = high
        self.order = order

        
        # Filters - 1. A notch filter to remove electrical interference (60Hz noise) and A bandpass filter (8-12Hz)
        self.b_notch, self.a_notch = iirnotch(self.notch_freq, self.notch_q, fs = self.sampling_rate)
        self.b_band, self.a_band = butter(self.order, [self.low, self.high], btype='band', fs = self.sampling_rate)
        # only have 1 channel
        self.zi_notch = None
        self.zi_band = None

    def process(self, x):
        """
        filter the input signal x with a notch filter followed by a bandpass filter
        args:
            x: a single sample or a 1-D array of samples (raw EEG)
        returns:
            y: the filtered signal (notch + bandpass)
        """

        x = np.atleast_1d(x).astype(float)
        if self.zi_notch is None:
            self.zi_notch = lfilter_zi(self.b_notch, self.a_notch) * x[0]
            self.zi_band = lfilter_zi(self.b_band, self.a_band) * x[0]
        notch_filtered, self.zi_notch = lfilter(self.b_notch, self.a_notch, x, zi=self.zi_notch)
        y, self.zi_band = lfilter(self.b_band, self.a_band, notch_filtered, zi=self.zi_band)
        return y