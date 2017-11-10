#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

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
    array = abs(array)/4096.
    return np.clip(array,10**(amp/20.),None) -10**(amp/20.)
    
def harmonique(array):
    fondamentale = []
    for i,o in enumerate(array):
        if o:
            if 0 in i % np.array(fondamentale):
                pass
            else:
                fondamentale.append(i)
    return fondamentale
    
space = np.linspace(0,1,44100)
signal = np.sin(1000*np.pi*2*space) + np.sin(1500*np.pi*2*space)