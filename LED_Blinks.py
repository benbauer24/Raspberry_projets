"""
This code file performs LED blinks using RPi 4

"""


import RPi.GPIO as GPIO
import time

led_pin = 17


def setup():                                      #Function to set GPIO numbering mode and pin configuration
    GPIO.setmode(GPIO.BCM)                        # Setting the GPIO numbering mode to BCM
    GPIO.setup(led_pin, GPIO.OUT)                 # LED pin set to output mode
    GPIO.output(led_pin, GPIO.LOW)                # Let Pin initially power off
    print(f"LED set on GPIO ID: {led_pin}")


def blink():                                      # Function to perform LED blinking in a looping way
    while True:
        GPIO.output(led_pin, GPIO.HIGH)        
        time.sleep(1)
        print("The LED is on >>>")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)
        print("The LED is off <<<")

def clear():                                      # Fiunction to clear and cleanup the code at the end
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":

    print("Led blinking code is running ")

    setup()

    try:
        blink()
    
    except KeyboardInterrupt:
        clear()

