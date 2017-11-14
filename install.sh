apt-get install python-pip libasound2-dev libjack-dev gfortran
wget https://pypi.python.org/packages/52/b6/44871791929d9d7e11325af0b7be711388dfeeab17147988f044a41a6d83/pyalsaaudio-0.8.4.tar.gz
tar xvzf pyalsaaudio-0.8.4.tar.gz
cd pyalsaaudio-0.8.4/
python setup.py install
pip install mido python-rtmidi numpy scipy
cd ..
rm -r pyalsaaudio-0.8.4/ pyalsaaudio-0.8.4.tar.gz
cd ext
f2py -c peak_location.f90 -m peak_location
cd ..
