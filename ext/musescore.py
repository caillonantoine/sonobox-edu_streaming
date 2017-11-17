# -*- coding: utf-8 -*-
from time import sleep
try: #ON ESSAYE D'IMPORT MIDO
    import mido as md
    mido = True
except:
    print "Librairie mido non installée, les fonctions midi ne seront pas utilisables. \n"
    sleep(3)
    mido = False

from time import sleep as wait

class MuseScore(object):
    """Classe contenant des méthodes permettant une écriture simplifiée des générations d'information MIDI
    """
    def __init__(self):
        self.midi_output = md.open_output('pythonout',virtual=True)
    def send(self,note):
        """Envoie un signal de note_on et note_off pour chaque note passée en argument
        """
        for elm in note:
            self.midi_output.send(md.Message('note_on',note=elm))
        for elm in note:
            self.midi_output.send(md.Message('note_off',note=elm))
        print "sent {}".format(note)
    def close(self):
        self.midi_output.close()

if mido:
    muse = MuseScore()
else:
    class NotMuse(object):
        """Emule un envoi midi en affichant sur le terminal la note qui aurait été envoyée dans le 
        cadre d'une utilisation optimale du programme.
        Si les librairies rt-midi et mido sont installées, les notes sont vraiment envoyées.
        """
        def send(self,note):
            for elm in note:
                print "NOTE MIDI = {}".format(elm)
    muse = NotMuse()