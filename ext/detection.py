#coding:utf-8
import numpy as np
from time import sleep

try: #ON ESSAYE D'IMPORTER LE MODULE FORTRAN
    from ext.pfm import detection
    fortran = True
except:
    fortran = False
    print "Module Fortran non trouvé,\n\
Si vous souhaitez maximiser les performances, pensez à compiler\n\
\"ext/peak_from_max.f90\" en \"pfm\" via f2py.\n Autrement, il y a un gros risque de\
perte d'échantillons.\n"
    sleep(3)
    def detection(array):
        """Définition d'un module de remplacement du module fortran.
        Fonctionnement rigoureusement identique, à l'exception du nombre d'itérations.
        L'utilisation de cette implémentation de l'algorithme entrainera des ralentissements
        ainsi que despertes de paquet d'échantillons, du à la lenteur de son execution.
        """
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
    """Fonction qui met à 0 toutes les valeurs inférieur à amp (en dBFS)
    """
    return np.clip(array,10**(amp/20.),None) -10**(amp/20.)
    
def harmonique(array):
    """
    Cherche la présence d'harmoniques (i.e de multiples d'une fondamentale) dans une liste de fréquence.
    """
    fondamentale = []
    array.sort()
    for elm in array:
        if fondamentale:
            if np.min(abs(elm % np.array(fondamentale))) != 0:
                fondamentale.append(elm)
        else:
            fondamentale.append(elm)
    
    return np.concatenate([fondamentale,np.zeros(20-len(fondamentale))])
