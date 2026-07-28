"""
ultrasonic.py
HC-SR04 Ultrasonic Sensor Library
Raspberry Pi Pico W (MicroPython)

Author: Pasam Jayasurya
"""

from machine import Pin
import utime
import config


class Ultrasonic:

    SPEED_OF_SOUND = 34300  # cm/s

    def __init__(self):

        self.trigger = Pin(config.TRIG_PIN, Pin.OUT)
        self.echo = Pin(config.ECHO_PIN, Pin.IN)

        self.trigger.low()
        utime.sleep_ms(2)

    # -------------------------------------------------
    # Raw Distance Measurement
    # -------------------------------------------------

    def _measure(self):

        # Send Trigger Pulse
        self.trigger.low()
        utime.sleep_us(2)

        self.trigger.high()
        utime.sleep_us(10)
        self.trigger.low()

        timeout = 30000

        start = utime.ticks_us()

        while self.echo.value() == 0:
            if utime.ticks_diff(utime.ticks_us(), start) > timeout:
                return None

        pulse_start = utime.ticks_us()

        while self.echo.value() == 1:
            if utime.ticks_diff(utime.ticks_us(), pulse_start) > timeout:
                return None

        pulse_end = utime.ticks_us()

        duration = utime.ticks_diff(pulse_end, pulse_start)

        distance = (duration * 0.0343) / 2

        return distance

    # -------------------------------------------------
    # Average Distance
    # -------------------------------------------------

    def distance(self, samples=5):

        readings = []

        for _ in range(samples):

            d = self._measure()

            if d is not None:
                readings.append(d)

            utime.sleep_ms(30)

        if len(readings) == 0:
            return 400

        return round(sum(readings) / len(readings), 2)

    # -------------------------------------------------
    # Obstacle Detection
    # -------------------------------------------------

    def obstacle(self):

        return self.distance() <= config.SAFE_DISTANCE

    # -------------------------------------------------
    # Immediate Stop Required
    # -------------------------------------------------

    def emergency_stop(self):

        return self.distance() <= config.STOP_DISTANCE

    # -------------------------------------------------
    # Print Distance
    # -------------------------------------------------

    def print_distance(self):

        d = self.distance()

        print("Distance: {:.2f} cm".format(d))

    # -------------------------------------------------
    # Continuous Monitor
    # -------------------------------------------------

    def monitor(self):

        try:

            while True:

                self.print_distance()

                utime.sleep(0.2)

        except KeyboardInterrupt:

            print("Monitoring stopped.")

    # -------------------------------------------------
    # Minimum Distance
    # -------------------------------------------------

    def minimum_distance(self, samples=10):

        values = []

        for _ in range(samples):

            d = self._measure()

            if d is not None:
                values.append(d)

            utime.sleep_ms(20)

        if not values:
            return 400

        return min(values)

    # -------------------------------------------------
    # Maximum Distance
    # -------------------------------------------------

    def maximum_distance(self, samples=10):

        values = []

        for _ in range(samples):

            d = self._measure()

            if d is not None:
                values.append(d)

            utime.sleep_ms(20)

        if not values:
            return 400

        return max(values)

    # -------------------------------------------------
    # Median Distance
    # -------------------------------------------------

    def median_distance(self, samples=7):

        values = []

        for _ in range(samples):

            d = self._measure()

            if d is not None:
                values.append(d)

            utime.sleep_ms(20)

        if not values:
            return 400

        values.sort()

        return values[len(values)//2]

    # -------------------------------------------------
    # Test Sensor
    # -------------------------------------------------

    def test(self):

        print("HC-SR04 Test Started")

        try:

            while True:

                d = self.distance()

                print("Distance = {:.2f} cm".format(d))

                if d < config.STOP_DISTANCE:
                    print("WARNING: Obstacle Very Close!")

                elif d < config.SAFE_DISTANCE:
                    print("Obstacle Detected")

                else:
                    print("Path Clear")

                utime.sleep(0.5)

        except KeyboardInterrupt:

            print("Sensor Test Finished")
