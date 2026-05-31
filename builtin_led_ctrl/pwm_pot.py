from machine import Pin, PWM, ADC
import time

a0 = ADC(0)
led = Pin(2, Pin.OUT)
led_pwm = PWM(led, freq = 1000)

def a0_get (sample_size = 20, time_window = 80):
    delay_value = time_window // sample_size
    mean = 0
    for _ in range(sample_size):
        mean += a0.read()
        time.sleep_ms(delay_value)
    return mean // sample_size

while True:
    a0_raw = a0_get()
    led_pwm.duty(a0_raw)
    time.sleep_ms(20)