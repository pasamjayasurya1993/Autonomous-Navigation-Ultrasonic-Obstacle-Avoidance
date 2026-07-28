"""
navigation.py
Autonomous Navigation Logic
Raspberry Pi Pico W + HC-SR04 + SG90 + L298N

Author: Pasam Jayasurya
"""

import utime

import config
from motors import MotorController
from ultrasonic import Ultrasonic
from servo import Servo


class Navigator:

    def __init__(self):

        self.motor = MotorController()
        self.sensor = Ultrasonic()
        self.servo = Servo()

        self.left_distance = 0
        self.right_distance = 0
        self.front_distance = 0

        self.running = True

        self.servo.center()

    # ------------------------------------
    # Read Front Distance
    # ------------------------------------

    def front(self):

        self.servo.center()

        utime.sleep(0.2)

        self.front_distance = self.sensor.distance()

        return self.front_distance

    # ------------------------------------
    # Scan Left
    # ------------------------------------

    def scan_left(self):

        self.servo.left()

        utime.sleep(0.4)

        self.left_distance = self.sensor.distance()

        return self.left_distance

    # ------------------------------------
    # Scan Right
    # ------------------------------------

    def scan_right(self):

        self.servo.right()

        utime.sleep(0.4)

        self.right_distance = self.sensor.distance()

        return self.right_distance

    # ------------------------------------
    # Scan Environment
    # ------------------------------------

    def scan(self):

        left = self.scan_left()

        right = self.scan_right()

        self.servo.center()

        return left, right

    # ------------------------------------
    # Choose Best Direction
    # ------------------------------------

    def choose_direction(self):

        left, right = self.scan()

        print("-------------------------")
        print("Left :", left)
        print("Right:", right)
        print("-------------------------")

        if left > right:

            return "LEFT"

        elif right > left:

            return "RIGHT"

        else:

            return "BACK"

    # ------------------------------------
    # Move Forward
    # ------------------------------------

    def forward(self):

        self.motor.normal_speed()

        self.motor.forward()

    # ------------------------------------
    # Stop Robot
    # ------------------------------------

    def stop(self):

        self.motor.stop()

    # ------------------------------------
    # Reverse Robot
    # ------------------------------------

    def reverse(self):

        print("Reverse")

        self.motor.backward()

        utime.sleep(config.REVERSE_TIME)

        self.motor.stop()

    # ------------------------------------
    # Turn Left
    # ------------------------------------

    def turn_left(self):

        print("Turning Left")

        self.motor.left()

        utime.sleep(config.TURN_TIME)

        self.motor.stop()

    # ------------------------------------
    # Turn Right
    # ------------------------------------

    def turn_right(self):

        print("Turning Right")

        self.motor.right()

        utime.sleep(config.TURN_TIME)

        self.motor.stop()

    # ------------------------------------
    # Rotate 180°
    # ------------------------------------

    def turn_back(self):

        print("Turning Around")

        self.motor.right()

        utime.sleep(config.TURN_TIME * 2)

        self.motor.stop()

    # ------------------------------------
    # Display Status
    # ------------------------------------

    def status(self):

        print("=========================")
        print("Front :", self.front_distance)
        print("Left  :", self.left_distance)
        print("Right :", self.right_distance)
        print("=========================")

    # ------------------------------------
    # Avoid Obstacle
    # ------------------------------------

    def avoid(self):

        self.stop()

        utime.sleep(0.2)

        direction = self.choose_direction()

        if direction == "LEFT":

            self.turn_left()

        elif direction == "RIGHT":

            self.turn_right()

        else:

            self.reverse()

            self.turn_back()

    # ------------------------------------
    # Check Path
    # ------------------------------------

    def path_clear(self):

        distance = self.front()

        if distance > config.SAFE_DISTANCE:

            return True

        return False
