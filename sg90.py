from machine import Pin, PWM
import time

duty_max = 65535
deg_min = 0.025 # -90
deg_middle = 0.0725 # 0
deg_max = 0.12 # 90

# init
def init(pin_pwm = 0, freq = 50):
    global servo
    servo = PWM(Pin(pin_pwm))
    servo.freq(freq)

# example function
def example(interval = 3):
    servo.duty_u16(round(duty_max * deg_min))
    time.sleep(interval)
        
    servo.duty_u16(round(duty_max * deg_middle))
    time.sleep(interval)
        
    servo.duty_u16(round(duty_max * deg_max))
    time.sleep(interval)