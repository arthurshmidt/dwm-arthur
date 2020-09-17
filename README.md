# dwm-arthur
My implementation of dwm

## Software

urxvt - Terminal Application
feh - get bactround image
xrdb - reload Xresources file
python3 - scripting
python3 (battery library) - psutil

## Patching

    $ patch -p1 < path/to/patch.diff

### Patches
* dwm-fullgaps-6.2.diff - allows for gaps between windows.
* dwm-barpadding-6.2.diff - creates gaps around the status bar.
* dwm-sticky-6.1.diff - allows windows to appear on all tags.

## File Locations

* dwm.desktop - /usr/share/xsessions/dwm.desktop
* dwm-startup - /usr/local/bin/dwm-startup
* dwm - /usr/local/bin/dwm
* dwm-bar-rc.py - /home/arthur/.config/dwm/dwm-bar-rc.py
