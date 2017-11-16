#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

signal = [0,0,0,0,0,0,1,2,3,4,3,2,1,0,0,0,0,0,0,1,2,1,0,0,0,0,1,2,3,0,0,0]
signal = np.asarray(signal,dtype=float)
signal = signal / np.max(signal)

def detection(array):
    freq = []
    i = 0
    o = 0
    for k in range(10):
        t = 1 - k/10.
        for ind,val in enumerate(array):
            if val >= t and i == 0:
                i = ind
            elif val < t and i != 0:
                o = ind
            
            if i != 0 and o != 0:
                mes = np.argmax(array[i:o]) + i
                if mes in freq:
                    i,o = 0,0
                else:
                    freq.append(mes)
                    i,o = 0,0
    return freq
    
def seuil(amp,array):
    return np.clip(array,10**(amp/20.),None) -10**(amp/20.)
    
def harmonique(array):
    fondamentale = []
    for elm in array:
        if fondamentale:
            if np.min(abs(elm % np.array(fondamentale))) != 0:
                fondamentale.append(elm)
        else:
            fondamentale.append(elm)
    return fondamentale