# SG-90
Library of stepper motor SG-90.

## Methods
```python
init(pin_pwm, freq)
```
Initial configuration.  
**pin_pwm** : pwm line (orange)  
**freq** : 50 (from data sheet)

```python
set_angle(angle = 90)
```
Set angle. (The parameters range from 0 to 180.)

## Example Main Function
```python
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
```