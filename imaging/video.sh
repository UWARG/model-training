#!/bin/bash

TIME="${date +%s}"
echo $TIME
ffmpeg -f v4l2 -framerate 30 -video_size 1920x1200 -input_format mjpeg -i /dev/video0 -c copy $TIME.mkv -y
