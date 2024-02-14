#!/bin/bash

# Update loop
while true; do
	# Battery life
	# xsetroot -name "$(echo -e '\uf240')  $(cat /sys/class/power_supply/BAT0/capacity)%"
	bat_icon=$(echo -e '\uf240')
	bat_percent=$(cat /sys/class/power_supply/BAT0/capacity)%
	wifi_icon=$(echo -e '\uf1eb')
	wifi_name=$(nmcli device status | grep connected | grep wifi | awk '{print $4}')
	date_time=$(date | awk '{print $1" "$2" "$3" "$4}')

	xsetroot -name " $wifi_icon  $wifi_name  < $bat_icon  $bat_percent < $date_time"

	sleep 2
done
