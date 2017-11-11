apt-get install python-pip spyder libasound2-dev libjack-dev musescore
wget https://pypi.python.org/packages/52/b6/44871791929d9d7e11325af0b7be711388dfeeab17147988f044a41a6d83/pyalsaaudio-0.8.4.tar.gz
tar xvzf pyalsaaudio-0.8.4.tar.gz
cd pyalsaaudio-0.8.4/
python setup.py install
pip install mido python-rtmidi numpy matplotlib scipy
cd ..
rm -r pyalsaaudio-0.8.4/ pyalsaaudio-0.8.4.tar.gz
