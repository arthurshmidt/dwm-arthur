#!/bin/sh

~/Src/dwm-arthur/dwm-6.4/scripts/bar-update.sh &
# xrdb ~/.Xresources &
feh --bg-fill ~/Src/dwm-arthur/minimal-pacman-wallpaper.jpg &

exec dwm
