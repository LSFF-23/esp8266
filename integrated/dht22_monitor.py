from machine import Pin, I2C, ADC
import dht
import ssd1306
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

dht_sensor = dht.DHT22(Pin(14))
potentiometer = ADC(0)
alert_led = Pin(12, Pin.OUT, value=0)

print("Temperature Monitor On.")

while True:
    try:
        dht_sensor.measure()
        current_temp = dht_sensor.temperature()
        current_humidity = dht_sensor.humidity()

        pot_value = potentiometer.read()
        temp_threshold = 20 + (pot_value / 1024) * (40 - 20)

        if current_temp > temp_threshold:
            alert_led.high()
            alert_status = "ALERT!"
        else:
            alert_led.low()
            alert_status = "OK"

        display.fill(0)
        display.text(f"MONITOR [{alert_status}]", 0, 0)
        display.hline(0, 10, 128, 1)
        display.text(f"Temp: {current_temp:.1f} C", 0, 18)
        display.text(f"Humidity: {current_humidity:.1f} %", 0, 32)
        display.hline(0, 48, 128, 1)
        display.text(f"Threshold: {temp_threshold:.1f} C", 0, 54)
        display.show()

    except OSError as e:
        display.fill(0)
        display.text("Read Error", 0, 20)
        display.text("on DHT sensor...", 0, 35)
        display.show()
        print("Failed to read DHT22 sensor.")

    time.sleep(2.0)