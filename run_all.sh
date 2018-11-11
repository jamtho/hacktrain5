#!/bin/bash

python /app/staffapp_server.py    &
python /app/tinkercatch_server.py &
python /app/hvaccontrol_server.py
