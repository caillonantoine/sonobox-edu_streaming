#coding:utf-8
import numpy as np
from ext import musescore as ms
from ext import soundcard as sc
from ext import detection as dt

#%%

def pad(array):
    if len(array) > 2**16:
        print "TROP GRAND"
        return array
    else:
        y = np.zeros(2**16)
        y[0:len(array)] = array
        return y
        
def get_midi_note_from_f(f):
    midi_scale = 110*np.power(2,np.array(range(120))/12.)
    midi_note = np.array(range(120))+45
    return midi_note[np.argmin(abs(midi_scale - f))]-12
        
def analyse():
    signal_in = sc.init_sound_card(512)
    for elm in signal_in:
        s_ = abs(np.fft.rfft(pad(elm)))
        f = dt.harmonique(dt.detection(dt.seuil(-35,s_)))
        f = np.array(f)*44100/float(2**16)
        print f
        
            
if __name__ == "__main__":
    pass