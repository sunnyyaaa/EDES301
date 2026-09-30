# -*- coding: utf-8 -*-


"""Blink the PocketBeagle USR3 LED at approximately 5 Hz.

Each cycle has 0.1 seconds on and 0.1 seconds off.
Press Ctrl+C to stop and turn the LED off.
"""

import time
import Adafruit_BBIO.GPIO as GPIO

LED = "USR3"
HALF_PERIOD = 0.1


def main():
    """Configure the LED and blink until interrupted."""
    GPIO.setup(LED, GPIO.OUT)

    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(HALF_PERIOD)

            GPIO.output(LED, GPIO.LOW)
            time.sleep(HALF_PERIOD)

    except KeyboardInterrupt:
        print("Stopped.")

    finally:
        GPIO.output(LED, GPIO.LOW)
        GPIO.cleanup()


if __name__ == "__main__":
    main()