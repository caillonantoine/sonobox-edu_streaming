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