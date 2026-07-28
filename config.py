"""
config.py
Configuration settings for Raspberry Pi Pico W Autonomous Robot Car
"""

# ==========================
# Ultrasonic Sensor Pins
# ==========================
TRIG_PIN = 2
ECHO_PIN = 3

# ==========================
# Servo Pin
# ==========================
SERVO_PIN = 15

# ==========================
# Motor Driver Pins (L298N)
# ==========================
LEFT_IN1 = 6
LEFT_IN2 = 7
RIGHT_IN1 = 8
RIGHT_IN2 = 9

LEFT_EN = 10
RIGHT_EN = 11

# ==========================
# PWM Settings
# ==========================
PWM_FREQ = 1000
MOTOR_SPEED = 50000      # 0–65535
TURN_SPEED = 45000

# ==========================
# Navigation Settings
# ==========================
SAFE_DISTANCE = 30        # cm
STOP_DISTANCE = 15        # cm

TURN_TIME = 0.55
REVERSE_TIME = 0.45

# ==========================
# Servo Angles
# ==========================
SERVO_LEFT = 150
SERVO_CENTER = 90
SERVO_RIGHT = 30

# ==========================
# Servo PWM Values
# (50Hz SG90)
# ==========================
SERVO_MIN = 1638
SERVO_MAX = 8192

# ==========================
# Delay Settings
# ==========================
SCAN_DELAY = 0.5
MAIN_LOOP_DELAY = 0.05
