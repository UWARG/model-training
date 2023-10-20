#!/bin/bash

# Colour calibration 2023-10-12
v4l2-ctl -d /dev/video0 --set-ctrl hue=-128
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_automatic=0
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_temperature=6500
v4l2-ctl -d /dev/video0 --set-ctrl auto_exposure=1

# Comment out one of the following

# OpenCV Python
touch /home/warg/record.log  # To confirm script has run
cd /home/warg/model-training/
source venv/bin/activate
cd imaging/
python -m imaging

# FFMPEG video
# touch /home/warg/record.log  # To confirm script has run
# cd /home/warg/model-training/imaging/
# ./video.sh