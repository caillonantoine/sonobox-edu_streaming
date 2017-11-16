# sonobox-edu_streaming
PROJET 4AA03

Transformer un sifflement en une information MIDI pour pouvoir afficher à l'écran les notes sifflées.

### Dépendances nécessaires
- alsaaudio (python)
- numpy
- mido
- python-rtmidi
- musescore pour l'affichage

### Installation

Installation sur Ubuntu (ou tout autre distribution basée sur debian):
- cloner le dépôt dans un repertoire
- lancer le script "install.sh" en administrateur, i.e:
```sh
sudo ./install.sh
```
Ce script installera les différentes dépendances requises ainsi que les logiciels SPYDER et MUSESCORE.

### Plateforme
Ce logiciel est écrit en utilisant des librairies fonctionnant sur Linux. Pour une compatibilité avec Windows, il faut remplacer la partie alsaaudio par pyaudio. 
