IP Camera IR LED automation script
==================================

This script is used to automatically turn off IP camera IR LEDs when the
observatory roof is open at Komakallio.

Before running the script for the first time, copy example config file
to `config.ini` and fill out all the fields:
```
cp config.ini.example config.ini
vim config.ini
```

The script can be run by executing:
```
python ip-cam-automation.py
```
