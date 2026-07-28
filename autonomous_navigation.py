    # ------------------------------------
    # Main Navigation Loop
    # ------------------------------------

    def run(self):

        print("================================")
        print(" Autonomous Navigation Started ")
        print("================================")

        self.running = True

        try:

            while self.running:

                distance = self.front()

                print("Front Distance:", distance, "cm")

                # -------------------------
                # Safe
                # -------------------------
                if distance > config.SAFE_DISTANCE:

                    self.forward()

                # -------------------------
                # Obstacle Ahead
                # -------------------------
                elif distance > config.STOP_DISTANCE:

                    print("Obstacle Detected")

                    self.avoid()

                # -------------------------
                # Emergency
                # -------------------------
                else:

                    print("Emergency Stop!")

                    self.stop()

                    utime.sleep(0.2)

                    self.reverse()

                    self.avoid()

                utime.sleep(config.MAIN_LOOP_DELAY)

        except KeyboardInterrupt:

            print("\nNavigation Stopped")

            self.stop()

            self.servo.center()

    # ------------------------------------
    # Patrol Mode
    # ------------------------------------

    def patrol(self):

        print("Patrol Mode")

        while True:

            if self.path_clear():

                self.forward()

            else:

                self.avoid()

            utime.sleep(0.05)

    # ------------------------------------
    # Servo Scan Test
    # ------------------------------------

    def scan_test(self):

        while True:

            left = self.scan_left()

            print("Left :", left)

            self.servo.center()

            utime.sleep(1)

            right = self.scan_right()

            print("Right:", right)

            self.servo.center()

            utime.sleep(1)

    # ------------------------------------
    # Sensor Test
    # ------------------------------------

    def sensor_test(self):

        while True:

            print("----------------")

            print("Front :", self.front())

            print("Left  :", self.scan_left())

            print("Right :", self.scan_right())

            self.servo.center()

            utime.sleep(1)

    # ------------------------------------
    # Motor Test
    # ------------------------------------

    def motor_test(self):

        print("Forward")

        self.motor.forward()

        utime.sleep(2)

        self.stop()

        print("Backward")

        self.motor.backward()

        utime.sleep(2)

        self.stop()

        print("Left")

        self.motor.left()

        utime.sleep(1)

        self.stop()

        print("Right")

        self.motor.right()

        utime.sleep(1)

        self.stop()

    # ------------------------------------
    # Full Hardware Test
    # ------------------------------------

    def self_test(self):

        print("===========================")
        print("Robot Self Test Started")
        print("===========================")

        self.motor_test()

        print("Servo Test")

        self.servo.test()

        print("Ultrasonic Test")

        for _ in range(5):

            print("Distance:", self.sensor.distance(), "cm")

            utime.sleep(1)

        print("Self Test Complete")

    # ------------------------------------
    # Stop Navigation
    # ------------------------------------

    def shutdown(self):

        self.running = False

        self.stop()

        self.servo.center()

        print("Robot Shutdown Complete")
