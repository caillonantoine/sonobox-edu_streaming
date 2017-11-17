#coding:utf-8
try:
    import alsaaudio as aa
    print "Utilisation du module alsa"
    alsa = True
except:
    print "module alsaaudio non trouvé, basculement sur pyaudio"
    sleep(3)
    try:
        import pyaudio as pa
        alsa = False
    except:
        raise Exception("Pyaudio ou alsaaudio indisponible. Executer install.sh pour resoudre les problemes.")
import numpy as np

if alsa:
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
            signal = sc.read()
            if signal[0] <= 0:
                print "MISSED FRAME"
            else:
                yield np.fromstring(signal[1],np.int16)/32767.
        sc.close()

else:
    def init_sound_card(chunk) : 
        CHUNK = chunk
        FORMAT = pa.paInt16
        CHANNELS = 1
        RATE = 44100
        
        p = pa.PyAudio()
        
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        while True:
            data = stream.read(CHUNK)
            echantillon = np.fromstring(data, dtype = np.int16)
            yield echantillon/32767.