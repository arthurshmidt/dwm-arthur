#!/bin/bash

# Update loop
while true; do
	# Battery life
	# xsetroot -name "$(echo -e '\uf240')  $(cat /sys/class/power_supply/BAT0/capacity)%"
	bat_icon=$(echo -e '\uf240')
	bat_percent=$(cat /sys/class/power_supply/BAT0/capacity)%
	wifi_icon=$(echo -e '\uf1eb')

	xsetroot -name " $wifi_icon  | $bat_icon  $bat_percent"

	sleep 2
done
