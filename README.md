Autonomous Navigation Using Ultrasonic Obstacle Avoidance

> A Raspberry Pi Pico W–based autonomous robot car that detects obstacles using an ultrasonic sensor and intelligently navigates around them using servo-based environmental scanning.

![Python](https://img.shields.io/badge/MicroPython-Compatible-blue)
![Raspberry Pi Pico W](https://img.shields.io/badge/Board-Raspberry%20Pi%20Pico%20W-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

# 📌 Overview

This project demonstrates an autonomous mobile robot capable of navigating unknown environments using an HC-SR04 ultrasonic distance sensor mounted on a servo motor. The robot continuously scans its surroundings, detects nearby obstacles, and automatically selects the safest direction before continuing its journey.

Designed for students, hobbyists, educators, and robotics enthusiasts, the project emphasizes clean, modular MicroPython code and easy hardware integration.

---

# ✨ Features

* Autonomous obstacle avoidance
* Real-time ultrasonic distance measurement
* Servo-based left/right environmental scanning
* Intelligent path selection
* Automatic reverse on close obstacles
* Smooth motor control using L298N
* Modular MicroPython architecture
* Easy to customize and extend
* GitHub-ready project structure
* Beginner-friendly documentation

---

# 🛠 Hardware Requirements

| Component                 | Quantity |
| ------------------------- | -------: |
| Raspberry Pi Pico W       |        1 |
| HC-SR04 Ultrasonic Sensor |        1 |
| SG90 Servo Motor          |        1 |
| L298N Motor Driver        |        1 |
| TT DC Gear Motors         |        2 |
| Robot Chassis             |        1 |
| Wheels                    |        2 |
| Caster Wheel              |        1 |
| Battery Pack (6–9V)       |        1 |
| Jumper Wires              |  Several |

---

# 📂 Project Structure

```text
Autonomous-Navigation-Ultrasonic-Obstacle-Avoidance/
│
├── main.py
├── navigation.py
├── motors.py
├── ultrasonic.py
├── servo.py
├── config.py
├── README.md
├── LICENSE
└── images/
    └── robot.jpg
```

---

# ⚙️ Working Principle

1. Robot moves forward.
2. Ultrasonic sensor continuously measures distance.
3. If the path is clear, the robot keeps moving.
4. When an obstacle is detected:

   * Stop immediately.
   * Rotate the servo to scan the left side.
   * Measure left-side distance.
   * Rotate the servo to scan the right side.
   * Measure right-side distance.
   * Compare both readings.
   * Turn toward the side with more free space.
5. Continue autonomous navigation.
6. Repeat indefinitely.

---

# 🧠 Navigation Logic

```text
Move Forward
      │
      ▼
Measure Distance
      │
      ▼
Obstacle?
 ┌──────────────┐
 │      No      │
 └──────┬───────┘
        │
Continue Forward

        Yes
        │
        ▼
Stop Robot
        │
        ▼
Scan Left
        │
        ▼
Scan Right
        │
        ▼
Compare Distances
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Turn Left   Turn Right
      │
      ▼
 Continue Forward
```

---

# 🚀 Getting Started

## 1. Assemble the Hardware

* Mount the Raspberry Pi Pico W on the robot chassis.
* Connect the L298N motor driver.
* Attach both DC motors.
* Install the HC-SR04 ultrasonic sensor on the SG90 servo.
* Connect the battery pack.

---

## 2. Install MicroPython

Flash the latest MicroPython firmware to the Raspberry Pi Pico W.

---

## 3. Upload Files

Copy all project files to the Pico W:

```
main.py
navigation.py
motors.py
ultrasonic.py
servo.py
config.py
```

---

## 4. Run the Robot

Restart the Pico W.

The robot will begin autonomous navigation automatically.

---

# ⚙️ Configuration

Example parameters:

```python
SAFE_DISTANCE = 30
STOP_DISTANCE = 15
TURN_TIME = 0.55
REVERSE_TIME = 0.45

SERVO_LEFT = 150
SERVO_CENTER = 90
SERVO_RIGHT = 30
```

Adjust these values according to your robot's speed, sensor placement, and operating environment.

---

# 🔌 Example GPIO Connections

| Device             | Pico GPIO |
| ------------------ | --------: |
| Ultrasonic Trigger |       GP2 |
| Ultrasonic Echo    |       GP3 |
| Servo Signal       |      GP15 |
| Motor IN1          |       GP6 |
| Motor IN2          |       GP7 |
| Motor IN3          |       GP8 |
| Motor IN4          |       GP9 |
| Motor Enable A     |      GP10 |
| Motor Enable B     |      GP11 |

---

# 📈 Future Enhancements

* Wi-Fi remote control
* Bluetooth control
* Line following mode
* Maze solving algorithms
* PID speed control
* OLED display
* Battery voltage monitoring
* Data logging
* Camera-based object detection
* SLAM and mapping
* Voice control
* Mobile application integration

---

# 🎯 Applications

* Robotics education
* STEM laboratories
* Engineering projects
* Autonomous vehicle research
* Embedded systems learning
* IoT demonstrations
* Robotics competitions
* Smart navigation prototypes

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

Please follow consistent coding standards and include documentation for new features.

---

# 📜 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# 👨‍💻 Author

**Pasam Jayasurya**

* M.Sc. Computer Science
* Raspberry Pi & Embedded Systems Enthusiast
* IoT and Robotics Developer
* Cybersecurity and Artificial Intelligence Researcher

---

# ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐞 Report issues
* 💡 Suggest improvements
* 📢 Share it with others

Your support helps improve the project and encourages future open-source development.
