#coding:utf-8
import alsaaudio as aa
import numpy as np

pcms = aa.pcms(aa.PCM_CAPTURE)
print "LISTE DES PERIPHERIQUES DISPONIBLES"

for i in range(len(pcms)):
	print "{} - {}".format(i,pcms[i])

device = pcms[int(raw_input("Tapez le numéro correspondant au périphérique choisi:\n"))]
print "\nLe périphérique utilisé est {}".format(device)

def init_sound_card(chunk_size):
    sc = aa.PCM(type=aa.PCM_CAPTURE,device=device)
    sc.setchannels(1)
    sc.setrate(44100)
    sc.setformat(aa.PCM_FORMAT_S16_LE)
    sc.setperiodsize(chunk_size)
    while True:
        yield np.fromstring(sc.read()[1],np.int16)/32767.
    sc.close()
        
        
    
    
def sin_init_sound_card(chunk):
    space = np.linspace(0,10,44100*20)
    signal = np.sin(1000*np.pi*2*space) + np.sin(1500*np.pi*2*space)
    for elm in range(44100*10/chunk):
        yield signal[elm*chunk:(elm+1)*chunk]