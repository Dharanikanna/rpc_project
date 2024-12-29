#!/bin/bash
# Setup virtual display
# Xvfb :99 -screen 0 1920x1080x24 &
# export DISPLAY=:99

# Check if /dev/video0 is free
if lsof /dev/video0; then
  echo "/dev/video0 is in use. Exiting."
  exit 1
fi

# Run libcamera-hello
libcamera-hello
