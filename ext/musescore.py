# -*- coding: utf-8 -*-
import mido as md
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

muse = MuseScore()