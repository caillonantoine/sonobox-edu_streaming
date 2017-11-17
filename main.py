#coding:utf-8
import numpy as np
from ext import musescore as ms
from ext import soundcard as sc
from ext import detection as dt
from time import sleep

#%%
class Notes(object):
    """Référence des fréquences et opère sur leur moyenne"""
    def __init__(self):
        self.freq = np.array([],dtype=float)
    def get_moy(self):
        return float(np.mean(self.freq))
    def get_size(self):
        return len(self.freq)
    def __add__(self,x):
        self.freq = np.append(self.freq,x)
        return self.freq
    def __radd__(self,x):
        return self.__add__(x)
    def __mod__(self,x):
        return np.mean(self.freq) % x
    def __rmod__(self,x):
        return self.__mod__(x)
    def __sub__(self,x):
        return np.mean(self.freq) - x
    def __rsub__(self,x):
        return self.__sub__(x)
    def __str__(self):
        return "{}".format(self.get_moy())


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
    notes = np.array([],dtype=Notes)
    for liste in freq:
        for f in liste:
            if f:
                if notes.any():
                    if (abs(f - notes) >= 50).all():
                        notes = np.append(notes,Notes())
                        notes[-1] + f
                    else:
                        ind = np.argmin(abs(f - notes))
                        notes[ind] + f
                else:
                    notes = np.append(notes,Notes())
                    notes[-1] + f
    w = np.array([elm.get_size() for elm in notes],dtype=float)
    w = w/np.max(w)
    y = []
    
    for i,o in enumerate(w):
        if o >= .5:
            y.append(get_midi_note_from_f(notes[i].get_moy()))
    ms.muse.send(np.array(y).astype('int'))
        
def analyse():
    chunk_size = 512
    signal_in = sc.init_sound_card(chunk_size)
    recorded_frequency = []
    for elm in signal_in:
        s_ = abs(np.fft.rfft(pad(elm)))
        s_ = 2*s_ / float(chunk_size)
        f = dt.harmonique(dt.detection(dt.seuil(-40,s_)))
        f = np.array(f)*44100/float(2**16)
        if f.any():
            recorded_frequency.append(f)
        elif not f.any() and recorded_frequency:
            check_and_send(recorded_frequency)
            recorded_frequency = []

            
if __name__ == "__main__":
    print "Pour démarrer l'analyse, entrer \"analyse()\""
    