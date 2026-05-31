from machine import Pin, PWM
import time

led = Pin(2, Pin.OUT)
led_pwm = PWM(led, freq = 1000)

while True:
    for i in range(1024):
        led_pwm.duty(i)
        time.sleep_ms(1)
    time.sleep_ms(500)
    
    for i in reversed(range(1024)):
        led_pwm.duty(i)
        time.sleep_ms(1)
    time.sleep_ms(500)