# sonobox-edu_streaming
PROJET 4AA03

Transformer des sifflements en informations MIDI pour pouvoir afficher à l'écran les notes sifflées.

### Dépendances nécessaires
- alsaaudio ou pyaudio
- numpy
- mido (interfaçage MIDI)
- python-rtmidi (nécessaire pour MIDI)
- musescore (Logiciel de partition libre)

### Installation

Installation sur Ubuntu (ou tout autre distribution basée sur debian):
- cloner le dépôt dans un repertoire
- lancer le script "install.sh" en administrateur, i.e:
```sh
sudo ./install.sh
```
Ce script installera les différentes dépendances requises.

### Plateforme
Ce logiciel est compatible Windows / macOS / Linux/
Le programme n'a pas été testé sous Mac (à défaut d'en avoir un), mais devrait fonctionner sans problème, sous réserve d'avoir les librairies nécessaires.
