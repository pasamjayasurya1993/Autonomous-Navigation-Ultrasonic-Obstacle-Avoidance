"""
main.py
Autonomous Navigation Robot
Raspberry Pi Pico W

Author: Pasam Jayasurya
"""

import utime
from navigation import Navigator


def main():

    print("=" * 40)
    print("Raspberry Pi Pico W Robot Car")
    print("Autonomous Obstacle Avoidance")
    print("=" * 40)

    robot = Navigator()

    utime.sleep(2)

    # Uncomment to test hardware
    # robot.self_test()

    # Start autonomous navigation
    robot.run()


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nProgram Terminated")
