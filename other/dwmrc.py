#!/usr/bin/python3

import psutil
import time
import os

def startup_apps():
    os.system("xrdb" + " ~/.Xresources" + "&")
    os.system("feh" + " --bg-scale" + " ~/Pictures/NGC6302.jpg" + " &")

def dwm_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged == False:
        plugged = "--"
    else:
        plugged = "++"

    return "{:.2F}% {}".format(percent,plugged)

def dwm_date():
    t = time.localtime()

    return time.strftime("%m/%d/%y %H:%M",t)

if __name__ == "__main__":
    
    startup_apps()
    
    while True:
        try:
            message = " < " + dwm_battery() + " < " + dwm_date()
            os.system("xsetroot" + " -name " + "'"+message+"'" )
        except:
            pass
        time.sleep(1)
