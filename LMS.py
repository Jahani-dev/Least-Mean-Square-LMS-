#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 16:41:10 2025

@author: Sahar Jahani

Description: A simulated ECG signal (1 Hz sinusoid) is corrupted with 50 Hz power line 
interference to test LMS (Least Mean Squares) adaptive filter performance.

The LMS algorithm adaptively removes the 50 Hz noise while preserving the 
ECG signal.


"""

import numpy as np
import matplotlib.pyplot as plt


fs1= 1 # ECG 1 Hz
fs2 = 50 # Electricity noise 50 Hz

t = np.linspace(0, 10, 300)
ECG = 0.5 * np.sin(2 * np.pi * fs1 * t) # model input
noise = 0.5 * np.sin(2 * np.pi * fs2 * t)

output = ECG + noise # model output = input signal + noise
x = np.sin(2 * np.pi * fs2 * t) # reference noise
w = 0

# mu < 1/(a0 * power of the input) 
p = np.mean(x**2)
# p = (1/len(x)) * (x @ x.T)
mu = 1 / (10 * p)

y = []
e = []
weight = np.zeros(len(x))

"LMS"
for i in range(len(x)):
    y_current = w * x[i]
    y.append(y_current)
    e_current = output[i] - y_current
    e.append(e_current)
    w = w + mu * e_current * x[i]
    weight[i] = w

e = np.array(e)

# Plot the results
plt.figure(figsize=(12, 10))


plt.subplot(4, 1, 1)
plt.plot(t, ECG, 'b-', label = "Simulated ECG signal")
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


plt.subplot(4, 1, 2)
plt.plot(t, output,'g-', label = "System Output _ Sensor measurement")
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 3)
plt.plot(t, e, 'r-', label = "LMS Estimate _ denoised ECG")
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 4)
plt.plot(t, weight, 'm-', label = "Weight Evolution", alpha=0.8)
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Weight Values')