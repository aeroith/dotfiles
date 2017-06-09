##!/bin/bash

((current = $(cat /sys/class/backlight/intel_backlight/actual_brightness)))
if [ $current -gt 200 ]
	then
	current=$((current-200))
else
	current=50
fi
tee /sys/class/backlight/intel_backlight/brightness <<< $current