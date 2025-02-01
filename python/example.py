from machine import Pin
import time
import sg90

# led
led = Pin("LED", Pin.OUT)
led.on()

if __name__ == "__main__":
    sg90.init()
    while True:
        sg90.set_angle(0)
        time.sleep(3)
        sg90.set_angle(90)
        time.sleep(3)
    pass