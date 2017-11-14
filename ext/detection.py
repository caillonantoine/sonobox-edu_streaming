#coding:utf-8
import numpy as np
import peak_location as pl

signal = [0,0,0,0,0,0,1,2,3,4,3,2,1,0,0,0,0,0,0,1,2,1,0,0,0,0,1,2,3,0,0,0]

def detection(array):
    array_pike = np.zeros_like(array)
    array = array * pl.detection(array,50,np.max(array))
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
    array = abs(array)/512.
    return np.clip(array,10**(amp/20.),None) -10**(amp/20.)
    
def harmonique(array):
    fondamentale = []
    for i,o in enumerate(array):
        if o:
            if i % np.array(fondamentale).any() <= 1:
                pass
            else:
                fondamentale.append(i)
    return fondamentale
    
space = np.linspace(0,1,44100)
signal = np.sin(1000*np.pi*2*space) + np.sin(1500*np.pi*2*space)

a = detection(abs(np.fft.rfft(signal)))