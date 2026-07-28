"""
servo.py
SG90 Servo Motor Library
Raspberry Pi Pico W (MicroPython)

Author: Pasam Jayasurya
"""

from machine import Pin, PWM
import utime
import config


class Servo:

    def __init__(self):

        self.pwm = PWM(Pin(config.SERVO_PIN))
        self.pwm.freq(50)

        self.current_angle = config.SERVO_CENTER

        self.move(config.SERVO_CENTER)

    # -----------------------------------------
    # Convert Angle to PWM Duty
    # -----------------------------------------

    def angle_to_duty(self, angle):

        angle = max(0, min(180, angle))

        duty = int(
            config.SERVO_MIN +
            (angle / 180) *
            (config.SERVO_MAX - config.SERVO_MIN)
        )

        return duty

    # -----------------------------------------
    # Move Servo
    # -----------------------------------------

    def move(self, angle):

        angle = max(0, min(180, angle))

        duty = self.angle_to_duty(angle)

        self.pwm.duty_u16(duty)

        self.current_angle = angle

        utime.sleep(config.SCAN_DELAY)

    # -----------------------------------------
    # Predefined Positions
    # -----------------------------------------

    def left(self):
        self.move(config.SERVO_LEFT)

    def center(self):
        self.move(config.SERVO_CENTER)

    def right(self):
        self.move(config.SERVO_RIGHT)

    # -----------------------------------------
    # Smooth Movement
    # -----------------------------------------

    def sweep(self, start, end, step=2, delay=0.02):

        if start < end:

            for angle in range(start, end + 1, step):
                self.pwm.duty_u16(self.angle_to_duty(angle))
                self.current_angle = angle
                utime.sleep(delay)

        else:

            for angle in range(start, end - 1, -step):
                self.pwm.duty_u16(self.angle_to_duty(angle))
                self.current_angle = angle
                utime.sleep(delay)

    # -----------------------------------------
    # Scan Left and Return
    # -----------------------------------------

    def scan_left(self):

        self.sweep(
            self.current_angle,
            config.SERVO_LEFT
        )

        return self.current_angle

    # -----------------------------------------
    # Scan Right and Return
    # -----------------------------------------

    def scan_right(self):

        self.sweep(
            self.current_angle,
            config.SERVO_RIGHT
        )

        return self.current_angle

    # -----------------------------------------
    # Center Servo Smoothly
    # -----------------------------------------

    def home(self):

        self.sweep(
            self.current_angle,
            config.SERVO_CENTER
        )

    # -----------------------------------------
    # Look Left
    # -----------------------------------------

    def look_left(self):

        self.left()

    # -----------------------------------------
    # Look Right
    # -----------------------------------------

    def look_right(self):

        self.right()

    # -----------------------------------------
    # Look Forward
    # -----------------------------------------

    def look_forward(self):

        self.center()

    # -----------------------------------------
    # Full Scan Demonstration
    # -----------------------------------------

    def scan_demo(self):

        print("Servo Scan Demo")

        while True:

            self.left()

            utime.sleep(0.5)

            self.center()

            utime.sleep(0.5)

            self.right()

            utime.sleep(0.5)

            self.center()

            utime.sleep(0.5)

    # -----------------------------------------
    # Continuous Sweep
    # -----------------------------------------

    def continuous_sweep(self):

        while True:

            self.sweep(30, 150)

            utime.sleep(0.2)

            self.sweep(150, 30)

            utime.sleep(0.2)

    # -----------------------------------------
    # Release Servo
    # -----------------------------------------

    def release(self):

        self.pwm.deinit()

    # -----------------------------------------
    # Test Routine
    # -----------------------------------------

    def test(self):

        print("Testing Servo...")

        self.center()
        utime.sleep(1)

        self.left()
        utime.sleep(1)

        self.center()
        utime.sleep(1)

        self.right()
        utime.sleep(1)

        self.center()

        print("Servo Test Complete")
