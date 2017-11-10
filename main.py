#coding:utf-8
import numpy as np
from ext import musescore as ms
from ext import soundcard as sc

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
    signal_in = sc.init_sound_card(4096)
    recorded_frequency = []
    for elm in signal_in:
        s_ = np.fft.rfft(pad(elm))
        f,A = np.argmax(abs(s_)),np.max(abs(s_))
        f,A = f*44100/float(2**16),20*np.log10(2*A/4096.)
        
        if A>=-25 and f>=700:   
            recorded_frequency.append(f)
        elif A<-25:
            if recorded_frequency:
                moyenne = np.mean(recorded_frequency)
                note = get_midi_note_from_f(moyenne)
                ms.muse.send(note)
                recorded_frequency = []
            
            
if __name__ == "__main__":
    analyse()