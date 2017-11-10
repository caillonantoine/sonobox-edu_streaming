#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

class CoupeBas():
    def __init__(self):
        self.x = np.zeros(5)
        self.y = np.zeros(5)
        self.alpha = 700/(float(2*44100))
    def filtre(self,array):
        x = np.concatenate([self.x,array])
        y = list(self.y)
        
        for n in range(len(x))[5:]:
            y.append((1/(1+self.alpha**4))*(x[n-4] - 4*x[n-3] + x[n-2] -4*x[n-1] + x[n]) -\
            (y[n-4] - 4* ((1-self.alpha**4)/(1+self.alpha**4))*y[n-3] + 6*y[n-2] \
            -4* ((1-self.alpha**4)/(1+self.alpha**4))*y[n-1]))
        
        self.x = x[-5:]
        self.y = y[-5:]
        return y[5:]
        
if __name__ == "__main__":
    space = np.linspace(0,1,44100)
    signal = np.sin(440*2*np.pi*space) + np.sin(440*2*2*np.pi*space) + np.sin(440*2*4*np.pi*space) + np.sin(440*2*6*np.pi*space)
    filtre = CoupeBas()
    signal_filtre = filtre.filtre(signal)
    plt.plot(signal_filtre)