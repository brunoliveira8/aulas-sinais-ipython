# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:39:16 2015

@author: bruno
"""
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

rate, samples = wavfile.read('Superman.wav')

#wavfile.write('Superman_lento.wav', rate/2, samples)


#wavfile.write('Superman_rapido.wav', rate*2, samples)

#wavfile.write('Superman_inv.wav', rate, samples[::-1])

#wavfile.write('Superman_ampl.wav', rate, 4*samples)


N = samples.shape[0]


slength = N/rate;
t = np.linspace(0, slength, num=N)
plt.subplot(5, 1, 1)
plt.plot(t, samples)
plt.title('Sem modificacao')

slength_slow = N/(rate/2);
t_slow = np.linspace(0, slength_slow, num=N)
plt.subplot(5, 1, 2)
plt.plot(t_slow, samples)
plt.title('Audio Rapido')


slength_fast = N/(2*rate);
t_fast = np.linspace(0, slength_fast, num=N)
plt.subplot(5, 1, 3)
plt.plot(t_fast, samples)
plt.title('Audio rapido')

slength_inv = N/rate;
t_inv = np.linspace(0, slength_inv, num=N)
plt.subplot(5, 1, 4)
plt.plot(t_fast, samples[::-1])
plt.title('Audio inverso')


plt.subplot(5, 1, 5)
plt.plot(t, 4*samples)
plt.title('Audio amplificado')

