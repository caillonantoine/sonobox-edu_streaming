#coding:utf-8
import numpy as np
import scipy.signal as sc

last = np.zeros(891)

def cvn2(x,y):
    #convole x et y en prenant en compte les 891 dernières valeurs de x
    global last
    x_last = pad(np.concatenate([last,x]))
    last = x[-891::]
    y = pad(y)
    return sc.fftconvolve(x_last,y,mode='valid')[len(pad(x)) - len(x)::]
    
    

def pad(array,n=1):
    #Fonction bourrage de zéro modifiée
    N = len(array)
    if n != 1:
        y = np.zeros(n)
        y[0:N] = array
        return y
    else:
        while 2**n < N:
            n += 1
        y = np.zeros(2**n)
        y[0:N] = array
        return y

    
nyq = 44100/2. #fréquence de nyquist
f1 = 700/nyq #fréquence de coupure
f2 = 5000/nyq #fréquence de coupure
width = 180/nyq #taille de la transition du filtre
gain = 60 #attenuation dans la bande rejetée
N,beta = sc.kaiserord(gain,width) #calcul de l'ordre du filtre pour satisfaire le gabarit

coef = sc.firwin(N+1,[f1,f2],width,window=('kaider',beta),pass_zero=False) #des coefs

if __name__ == "__main__": #PARTIE DE TEST
    space = np.linspace(0,1,44100)
    signal = sum([np.sin((i+1)*440*np.pi*2*space) for i in range(12)])
    
    def spectre(array):
        sp = abs(np.fft.rfft(array))
        sp = sp/np.max(sp)
        plt.plot(sp)
        plt.grid()
        plt.show()