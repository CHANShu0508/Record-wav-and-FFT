# -*- coding: utf-8 -*-

from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

class AudioAnalysis:
    filename = 'test.wav'
    sample_rate = 0 # per second
    samples = []
    sample_len = 0
    sample_time = 0
    time_vector = []
    fft_samples = []
    left_ray = []
    right_ray = []

    def __init__(self, filename):
        self.filename = filename
        self.sample_rate, self.samples = read(self.filename)
        self.sample_len = len(self.samples)
        self.sample_time = self.sample_len / self.sample_rate
        self.time_vector = np.linspace(0, self.sample_time, self.sample_len)
        print("Sampling rate: ", self.sample_rate)
        print("Total number of samples: ", self.sample_len)
        print("Total time in seconds: ", round(self.sample_time))
    
    def draw_time_domain(self):
        plt.figure(1)
        plt.subplot(2, 1, 1)
        plt.plot(self.time_vector, self.samples[:, 0], color = 'b')
        plt.title("Time domain: left side")
        plt.subplot(2, 1, 2)
        plt.plot(self.time_vector, self.samples[:, 1], color = 'r')
        plt.title("Time domain: right side")
        plt.xlabel('time(sec)')
        plt.ylabel('amplitude')

    def fast_fourier_trans(self):
        self.fft_samples = self.samples / (2.**15) #convert sound array to float pt. values
        self.left_ray = self.fft_samples[:, 0]
        self.right_ray = self.fft_samples[:, 1]

        fft_length = len(self.left_ray)
        left_fft = abs(fft(self.left_ray, fft_length))
        right_fft = abs(fft(self.right_ray, fft_length))
        fft_vector = fftfreq(round(self.sample_rate*self.sample_time), 1 / self.sample_rate)

        plt.figure(2)
        plt.subplot(2, 1, 1)
        plt.plot(fft_vector, left_fft, color = 'b')
        plt.title("Frequency domain: left side")
        plt.subplot(2, 1, 2)
        plt.plot(fft_vector, right_fft, color = 'r')
        plt.title("Frequency domain: right side")
        plt.xlabel('Freq')
        plt.ylabel('amplitude')
        plt.show()

