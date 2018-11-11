#!/bin/bash

python hvaccontrol_server.py &
python staffapp_server.py    &
python tinkercatch_server.py &
