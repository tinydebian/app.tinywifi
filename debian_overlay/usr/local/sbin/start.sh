#!/bin/bash

# Turn off status LED (GPIO A10)
echo 0 > /sys/class/leds/status_led/brightness

# Blink LED
/usr/local/sbin/blink_leds.py  &

sync
exit 0
