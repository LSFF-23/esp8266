esptool --port COM3 erase-flash
esptool --port COM3 --baud 460800 write-flash --flash-size=detect 0 .\esp8266.bin