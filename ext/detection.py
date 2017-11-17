#coding:utf-8
import numpy as np
from time import sleep
try:
    from ext.pfm import detection
except:
    print "Module Fortran non trouvé,\n\
Si vous souhaitez travailler en temps réel, pensez à compiler\n\
\"ext/peak_from_max.f90\" en \"pfm.so\"."
    sleep(3)
    def detection(array):
        freq = []
        i = 0
        o = 0
        for k in range(3):
            t = 1 - k/3.
            for ind,val in enumerate(array):
                if val >= t and i == 0:
                    i = ind
                elif val < t and i != 0:
                    o = ind
                
                if i != 0 and o != 0:
                    mes = np.argmax(array[i:o]) + i
                    if mes in freq:
                        i,o = 0,0
                    else:
                        freq.append(mes)
                        i,o = 0,0
        return freq

def seuil(amp,array):
    return np.clip(array,10**(amp/20.),None) -10**(amp/20.)
    
def harmonique(array):
    fondamentale = []
    for elm in array:
        if fondamentale:
            if np.min(abs(elm % np.array(fondamentale))) != 0:
                fondamentale.append(elm)
        else:
            fondamentale.append(elm)
    
    return np.concatenate([fondamentale,np.zeros(20-len(fondamentale))])
    
if __name__ == "__main__":
    print detection(signal)       
    print pfm.detection(signal)