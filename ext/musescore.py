# -*- coding: utf-8 -*-
import mido as md
from time import sleep as wait

class MuseScore(object):
    def __init__(self):
        self.midi_output = md.open_output('pythonout',virtual=True)
    def send(self,note):
        self.midi_output.send(md.Message('note_on',note=note))
        self.midi_output.send(md.Message('note_off',note=note))
    def close(self):
        self.midi_output.close()

        