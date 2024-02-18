#!/usr/bin/python
# This program is meant to update status bar for dwm

# import statements
import os
import time
import subprocess

# Flags
is_running = True

# general text 
space = " "
space_arrow = " < "

# time commands 
date_icon = ""
date_time = "$(date | awk '{print $1 $2 $3 $4}')" 

# Battery commands
bat_icon = "\uf240"
bat_command = "$(cat /sys/class/power_supply/BAT0/capacity)%"

# Wifi Commands
wifi_icon = "\uf1eb"
wifi_command = "$(nmcli device status | grep connected | grep wifi | awk '{print $4}')"

# Combined commands
command = ("xsetroot -name " + '"' + 
    space + wifi_icon + 2*space + wifi_command + 
    space_arrow + bat_icon + 2*space + bat_command + 
    space_arrow + date_time +'"'
)

# update loop and test if dwm closed out
# intended to kill processes that were started specifically 
# for dwm 
while is_running:
    #print(command)
    try:
        dwm_pid = subprocess.check_output(['pgrep','dwm'])
        os.system(command)
        is_running = True
    except:
        is_running = False
    #bar = os.system('pgrep -u arthur bar-update.py')
    #print(f"bar return {bar}")
    #pgrep_dwm = os.system('pgrep -u arthur dwm')
    #print(f"dwm return {dwm}")
    time.sleep(2)
