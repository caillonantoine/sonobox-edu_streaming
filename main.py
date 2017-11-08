#coding:utf-8
import numpy as np
from ext import musescore as ms
from ext import soundcard as sc

def pad(array):
    if len(array) > 2**16:
        print "TROP GRAND"
        return array
    else:
        y = np.zeros(2**16)
        y[0:len(array)] = array
        return y
        
def analyse():
    signal_in = sc.init_sound_card(4096)
    for elm in signal_in:
        s_ = np.fft.rfft(pad(elm))
        f,A = np.argmax(abs(s_)),np.max(abs(s_))
        f,A = f*44100/float(2**16),20*np.log10(2*A/4096.)

                
        
        if A>=-35:   
            result = "Fréquence: {} Hz, Amplitude: {} dBFS".format(int(f),int(A))
            print result
            
if __name__ == "__main__":
    analyse()