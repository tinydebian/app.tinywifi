#!/usr/bin/python3

import time

def led_write(value):
    try:
        with open('/sys/class/leds/status_led/brightness', 'w') as f:
            f.write(value)
    except IOError:
        pass

if __name__ == "__main__":
    while True:
        led_write('255')
        time.sleep(0.5)
        led_write('0')
        time.sleep(0.5)
