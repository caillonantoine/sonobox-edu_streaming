#coding:utf-8
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%                                         %"
print "%       4AA03 - SONOBOX STREAMING         %"
print "%                                         %"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

from time import sleep
sleep(1)

#IMPORT DES DIFFERENTS MODULES
import numpy as np
from ext import musescore as ms
from ext import soundcard as sc
from ext import detection as dt
from ext import filtre as fl


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
	#Fonction Bourrage de zéro

    if len(array) > 2**16:
        print "TROP GRAND"
        return array
    else:
        y = np.zeros(2**16)
        y[0:len(array)] = array
        return y
        
def get_midi_note_from_f(f):
	#Dresse un tableau des fréquences en fonction des notes midi, effectue la comparaison
	#avec f, et renvoie la note midi correspondante
    midi_scale = 110*np.power(2,np.array(range(120))/12.)
    midi_note = np.array(range(120))+45
    return midi_note[np.argmin(abs(midi_scale - f))]-12
    
def check_and_send(freq):
	#Tire parti de la classe Notes().
	#
	#Cette fonction va moyenner les différentes notes sifflées, afin de se rapprocher
	#de la valeur 'vraie' de la fréquence.
	#Elle élimine aussi les accidents. Si une harmonique est laissée par le filtre harmonique
	#sur un petit nombre de paquets, elle sera ignorée.

    notes = np.array([],dtype=Notes)
    for liste in freq:
        for f in liste:
            if f:
                if notes.any(): #TRI DES FREQUENCES EN FONCTION DES FREQUENCES DEJA REPERTORIEES
                    if (abs(f - notes) >= 100).all():
                        notes = np.append(notes,Notes())
                        notes[-1] + f
                    else:
                        ind = np.argmin(abs(f - notes))
                        notes[ind] + f
                else: #PAS DEFREQUENCE REPERTORIEE, ON AJOUTE DIRECTEMENT.
                    notes = np.append(notes,Notes())
                    notes[-1] + f
    w = np.array([elm.get_size() for elm in notes],dtype=float)
    w = w/np.max(w)
    y = []
    #On vérifie que la fréquence apparait suffisamment de fois:
    for i,o in enumerate(w):
        if o >= .5:
            y.append(get_midi_note_from_f(notes[i].get_moy()))
    ms.muse.send(np.array(y).astype('int'))
        
def analyse():
	#Cette fonction lance une boucle, va récuperer des données audio dans le module ext/soundcard
	#et va effectuer une transformée de fourier rapide de ces données, pour en suite traiter le signal
	#via les fonctions dt.seuil, dt.detection,dt.harmonique.
	#
	#Une fois les données traitées, si des fréquences sont détectées, on appelle la fonction check_and_send
	
    chunk_size = 512
    signal_in = sc.init_sound_card(chunk_size)
    recorded_frequency = []
    for elm in signal_in:
        elm = fl.cvn2(elm,fl.coef) #On ne garde que la bande 700-5000Hz
        s_ = abs(np.fft.rfft(pad(elm)))
        s_ = 2*s_ / float(chunk_size)
        f = dt.harmonique(dt.detection(dt.seuil(-40,s_)))
        f = np.array(f)*44100/float(2**16)
        if f.any():
            recorded_frequency.append(f)
        elif not f.any() and recorded_frequency:
            check_and_send(recorded_frequency)
            recorded_frequency = []

            
if __name__ == "__main__": #Cette partie est cosmétique, elle aide au paramétrage du programme.
    modules = []
    if dt.fortran:
        modules.append("optimisation du module de detection en Fortran")
    if sc.alsa:
        modules.append("alsaaudio (accès carte son)")
    else:
        modules.append("PyAudio (accès carte son)")
    if ms.mido:
        modules.append("Mido (Création de ports virtuels midi)")
        
    
    print "Les librairies suivantes ont été importées:\n   -{}\n".format("\n   -".join(modules))
    if dt.fortran and ms.mido:
        print "Le logiciel a été correctement configuré et fonctionne de manière optimale.\n\
Félicitations!\n"
    else:
        print "Le logiciel est en mesure de fonctionner, mais pas de manière optimale.\n\
Se réferrer au README.md pour s'informer de la liste des modules à installer."
    if raw_input("Commencer l'analyse? [y/n] ").upper() == "Y":
        print "Analyse commencée"
        analyse()
    else:
        print "Bye!"
