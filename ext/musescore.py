# -*- coding: utf-8 -*-
from time import sleep
try:
    import mideo as md
    mido = True
except:
    print "Librairie mido non installée, les fonctions midi ne seront pas utilisables. \n"
    sleep(3)
    mido = False
from time import sleep as wait

class MuseScore(object):
    def __init__(self):
        self.midi_output = md.open_output('pythonout',virtual=True)
    def send(self,note):
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
        def send(self,note):
            for elm in note:
                print "NOTE MIDI = {}".format(elm)
    muse = NotMuse()