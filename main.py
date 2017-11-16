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
    
def check_and_send(freq):
    print "PAS ENCORE IMPLEMENTE"
        
def analyse():
    signal_in = sc.init_sound_card(512)
    recorded_frequency = []
    for elm in signal_in:
        s_ = abs(np.fft.rfft(pad(elm)))
        s_ = s_ / 512.
        f = dt.harmonique(dt.detection(dt.seuil(-40,s_)))
        f = np.array(f)*44100/float(2**16)
        if list(f):
            recorded_frequency.append(f)
        else:
            check_and_send(recorded_frequency)
        

            
if __name__ == "__main__":
    pass