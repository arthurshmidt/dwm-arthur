#!/bin/sh

~/Dev/dwm-arthur/dwm-6.4/scripts/bar-update.py &
xrdb ~/.Xresources &
feh --bg-fill ~/Dev/dwm-arthur/minimal-pacman-wallpaper.jpg &

exec dwm
