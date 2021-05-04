#!/bin/sh

# Battery icon
cbatticon -u 5 &

# Volume icon
volumeicon &

#notifiactions
dunst &

# compositor
picom -b -f 

# Wallpaper
#feh --bg-fill /home/aaron/.Wallpapers/02.png

#Settings
#xsettingsd &

#Wifi manager
#nm-applet &
