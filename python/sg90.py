from machine import Pin, PWM

# parameters from data sheet
duty_max = 65025
angle_min = 0.025
angle_middle = 0.0725
angle_max = 0.12

# init
def init(pin_pwm = 0, freq = 50): # do not change freq
    global servo
    servo = PWM(Pin(pin_pwm))
    servo.freq(freq)

# set angle
def set_angle(angle = 90): # from 0 to 180
    duty = angle_min + (angle_max - angle_min) / 180 * angle
    servo.duty_u16(int(duty_max * duty))