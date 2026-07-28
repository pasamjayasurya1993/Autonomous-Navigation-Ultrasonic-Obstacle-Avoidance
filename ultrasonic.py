from machine import Pin
import time

TRIG = Pin(14, Pin.OUT)
ECHO = Pin(15, Pin.IN)

def get_distance():

    TRIG.low()
    time.sleep_us(2)

    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    timeout = 30000

    while ECHO.value() == 0:
        timeout -= 1
        if timeout <= 0:
            return None

    start = time.ticks_us()

    while ECHO.value() == 1:
        timeout -= 1
        if timeout <= 0:
            return None

    end = time.ticks_us()

    duration = time.ticks_diff(end, start)

    distance = (duration * 0.0343) / 2

    return distance
