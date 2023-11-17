#!/bin/bash

# Camera calibration
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_temperature=4600
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_automatic=1
v4l2-ctl -d /dev/video0 --set-ctrl auto_exposure=3

# OpenCV Python
touch /home/warg/record.log  # To confirm script has run  # TODO: Update
cd /home/warg/model-training/  # TODO: Update
source venv/bin/activate
cd imaging/  # TODO: Update
python -m imaging  # TODO: Update
