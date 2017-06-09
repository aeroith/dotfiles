##!/bin/bash

((current = $(cat /sys/class/backlight/intel_backlight/actual_brightness)))
if [ $current -lt 777 ]
	then
	current=$((current+200))
else
	current=976
fi
tee /sys/class/backlight/intel_backlight/brightness <<< $current