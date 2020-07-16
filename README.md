# dwm-arthur
My implementation of dwm

## Patching

    $ patch -p1 < path/to/patch.diff

### Patches
* dwm-fullgaps-6.2.diff - allows for gaps between windows.
* dwm-barpadding-6.2.diff - creates gaps around the status bar.
* dwm-sticky-6.1.diff - allows windows to appear on all tags.

## Software Dependencies / Needs

### Debian to compile
* sudo apt install libx11-dev
* sudo apt install libxft-dev
* sudo apt install libxinerama-dev

### General Software
* feh - background images
* pip3 psutils - startup script for bar settings
* urxvt - terminal
* .Xresources - Color scheme & urxvt terminal settings
