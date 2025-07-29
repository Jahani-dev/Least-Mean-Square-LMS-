# LMS Adaptive Filter for ECG Denoising

A Python implementation of the **Least Mean Squares (LMS) adaptive filter** for removing power line interference from simulated ECG signals.

## Overview

This project demonstrates how adaptive filtering can effectively remove 50 Hz power line interference from biomedical signals while preserving the underlying ECG information.
The LMS algorithm automatically learns and adapts to cancel out the noise component.

## Problem Statement

- **Clean Signal**: Simulated ECG at 1 Hz (representing heart rhythm)
- **Interference**: 50 Hz power line noise (common in medical environments)
- **Goal**: Remove the 50 Hz interference while preserving the ECG signal

## Algorithm

The **LMS (Least Mean Squares)** adaptive filter works by:

1. **Reference Signal**: Uses a 50 Hz reference signal correlated with the noise
2. **Adaptive Weight**: Continuously adjusts a filter weight `w` to minimize error
3. **Weight Update Rule**: `w(n+1) = w(n) + μ × e(n) × x(n)`
   - `μ` = learning rate (step size)
   - `e(n)` = error signal
   - `x(n)` = reference input

## Results

<img width="735" height="589" alt="ECG_Noise_Removal" src="https://github.com/user-attachments/assets/ef5b4203-b188-4359-a9d7-ab204fcc66de" />


The plots show:
- **Top**: Clean simulated ECG signal (1 Hz)
- **Middle**: Noisy ECG signal (1 Hz + 50 Hz interference)
- **Bottom**: LMS filtered output (denoised ECG)
- **Bottom**: Weight evolution showing filter convergence

### Key Parameters
- **ECG Frequency**: 1 Hz
- **Noise Frequency**: 50 Hz
- **Learning Rate**: μ = 1/(10 × signal_power)
- **Duration**: 10 seconds
- **Samples**: 300 points


## Educational Value

This project illustrates key concepts in:
- **Adaptive Signal Processing**
- **Biomedical Engineering**
- **Digital Filter Design**
- **Noise Cancellation Techniques**
- **Real-time Algorithm Implementation**

## 🔧 Technical Details

### Learning Rate Selection
The learning rate μ is automatically calculated using:
```python
signal_power = np.mean(reference_signal**2)
mu = 1 / (10 * signal_power)
```
This ensures filter stability and optimal convergence speed.

### Filter Convergence
The LMS algorithm typically converges within the first few samples, as evidenced by the weight evolution plot.

## Applications
This technique is widely used in:
- **Medical Devices**: ECG machines, patient monitors
- **Noise Cancellation**: Headphones, communication systems
- **Radar Systems**: Clutter removal
- **Seismic Processing**: Earthquake signal analysis
- **Audio Processing**: Echo cancellation

## Theory Background
The LMS algorithm minimizes the mean square error between:
- **Desired signal** d(n): Noisy ECG
- **Filter output** y(n): Adaptive filter response

**Cost Function**: J = E[e²(n)] where e(n) = d(n) - y(n)

The algorithm uses **stochastic gradient descent** to find the optimal filter weight.

## Extensions
Potential improvements and variations:
- **Multi-tap FIR filter**: For complex noise patterns
- **Normalized LMS (NLMS)**: Better convergence properties
- **Variable step-size**: Adaptive learning rate
- **Real ECG data**: Testing with actual physiological signals
- **Multiple interference frequencies**: 60 Hz + harmonics


## Author
**Sahar Jahani**  
- Email: [jahanisahar0@gmail.com]
-  LinkedIn: [   ]
