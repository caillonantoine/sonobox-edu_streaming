#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

signal = [0,0,0,0,0,0,1,2,3,4,3,2,1,0,0,0,0,0,0,1,2,1,0,0,0,0,1,2,3,0,0,0]

def detection(array):
    array_pike = np.zeros_like(array)
    little_array = []
    for i,o in enumerate(array):
        if o:
            little_array.append(o)
        elif little_array:
            argmax = np.argmax(little_array)
            array_pike[argmax+i-len(little_array)] = 1
            little_array = []
    return array_pike
    
def seuil(amp,array):
    return np.clip(np.asarray(array),10**(amp/20),None) - 10**(amp/20)
    
def harmonique(array):
    fondamentale = []
    for i,o in enumerate(array):
        if o:
            if 0 in i % np.array(fondamentale):
                pass
            else:
                fondamentale.append(i)
    return fondamentale
    
signal= wavfile.read('../siffle.wav')[1]/32767.
s_ = abs(np.fft.rfft(signal))/len(signal)