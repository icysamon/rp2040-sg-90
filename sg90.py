from machine import Pin, PWM
import time

duty_max = 65535
angle_min = 0.025　# -90度
angle_middle = 0.0725 # 0度
angle_max = 0.12 # 90度

# 初期化
def init(pin_pwm = 0, freq = 50):
    global servo
    servo = PWM(Pin(pin_pwm))
    servo.freq(freq)

# テスト
def example(interval = 3):
    servo.duty_u16(round(duty_max * angle_min))
    time.sleep(interval)
        
    servo.duty_u16(round(duty_max * angle_middle))
    time.sleep(interval)
        
    servo.duty_u16(round(duty_max * angle_max))
    time.sleep(interval)