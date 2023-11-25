#!/bin/bash

# Get current Unix time to avoid collision
# TODO: Something more sophisticated (e.g. counter)
TIME="${date +%s}"
echo $TIME

# FFMPEG video
cd /home/warg/model-training/  # Update to actual path
touch record_$TIME.log  # To confirm script has run
cd imaging/
ffmpeg -f v4l2 -framerate 30 -video_size 1920x1200 -input_format mjpeg -i /dev/video0 -c copy $TIME.mkv -y
