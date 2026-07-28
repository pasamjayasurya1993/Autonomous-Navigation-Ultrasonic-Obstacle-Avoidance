"""
motors.py
Motor control library for Raspberry Pi Pico W
Driver: L298N
Author: Pasam Jayasurya
"""

from machine import Pin, PWM
import config


class MotorController:

    def __init__(self):

        # Direction Pins
        self.left_in1 = Pin(config.LEFT_IN1, Pin.OUT)
        self.left_in2 = Pin(config.LEFT_IN2, Pin.OUT)

        self.right_in1 = Pin(config.RIGHT_IN1, Pin.OUT)
        self.right_in2 = Pin(config.RIGHT_IN2, Pin.OUT)

        # PWM Enable Pins
        self.left_pwm = PWM(Pin(config.LEFT_EN))
        self.right_pwm = PWM(Pin(config.RIGHT_EN))

        self.left_pwm.freq(config.PWM_FREQ)
        self.right_pwm.freq(config.PWM_FREQ)

        self.speed(config.MOTOR_SPEED)

        self.stop()

    # ---------------------------------
    # Speed
    # ---------------------------------

    def speed(self, value):

        value = max(0, min(65535, value))

        self.left_pwm.duty_u16(value)
        self.right_pwm.duty_u16(value)

    # ---------------------------------
    # Forward
    # ---------------------------------

    def forward(self):

        self.left_in1.high()
        self.left_in2.low()

        self.right_in1.high()
        self.right_in2.low()

    # ---------------------------------
    # Backward
    # ---------------------------------

    def backward(self):

        self.left_in1.low()
        self.left_in2.high()

        self.right_in1.low()
        self.right_in2.high()

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        self.left_in1.low()
        self.left_in2.low()

        self.right_in1.low()
        self.right_in2.low()

    # ---------------------------------
    # Turn Left
    # ---------------------------------

    def left(self):

        self.left_in1.low()
        self.left_in2.high()

        self.right_in1.high()
        self.right_in2.low()

    # ---------------------------------
    # Turn Right
    # ---------------------------------

    def right(self):

        self.left_in1.high()
        self.left_in2.low()

        self.right_in1.low()
        self.right_in2.high()

    # ---------------------------------
    # Forward Left
    # ---------------------------------

    def forward_left(self):

        self.left_pwm.duty_u16(config.TURN_SPEED)

        self.right_pwm.duty_u16(config.MOTOR_SPEED)

        self.forward()

    # ---------------------------------
    # Forward Right
    # ---------------------------------

    def forward_right(self):

        self.left_pwm.duty_u16(config.MOTOR_SPEED)

        self.right_pwm.duty_u16(config.TURN_SPEED)

        self.forward()

    # ---------------------------------
    # Reverse Left
    # ---------------------------------

    def reverse_left(self):

        self.left_pwm.duty_u16(config.TURN_SPEED)

        self.right_pwm.duty_u16(config.MOTOR_SPEED)

        self.backward()

    # ---------------------------------
    # Reverse Right
    # ---------------------------------

    def reverse_right(self):

        self.left_pwm.duty_u16(config.MOTOR_SPEED)

        self.right_pwm.duty_u16(config.TURN_SPEED)

        self.backward()

    # ---------------------------------
    # Restore Speed
    # ---------------------------------

    def normal_speed(self):

        self.left_pwm.duty_u16(config.MOTOR_SPEED)

        self.right_pwm.duty_u16(config.MOTOR_SPEED)

    # ---------------------------------
    # Emergency Brake
    # ---------------------------------

    def brake(self):

        self.stop()

    # ---------------------------------
    # Rotate Left
    # ---------------------------------

    def rotate_left(self):

        self.left()

    # ---------------------------------
    # Rotate Right
    # ---------------------------------

    def rotate_right(self):

        self.right()

    # ---------------------------------
    # Test Routine
    # ---------------------------------

    def test(self):

        import time

        print("Forward")
        self.forward()
        time.sleep(2)

        print("Backward")
        self.backward()
        time.sleep(2)

        print("Left")
        self.left()
        time.sleep(1)

        print("Right")
        self.right()
        time.sleep(1)

        print("Stop")
        self.stop()
