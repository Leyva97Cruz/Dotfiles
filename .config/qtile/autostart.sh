#!/bin/sh

# Battery icon
cbatticon -u 5 &

# Volume icon
volumeicon &

#notifiactions
dunst &

# compositor
picom -b -f 
