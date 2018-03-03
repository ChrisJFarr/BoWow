import serial
import struct
from time import sleep
from serial import SerialException
# from mobility.robot_drive.robot_drive_archived import RobotDriveArchived
# import keyboard


# Create robot drive class
# class RobotDrive(RobotDriveArchived):  # uncomment if archived methods are needed
class RobotDrive:
    
    def __init__(self, default_speed=80):
        # Start the serial port to communicate with arduino
        try:
            try:
                # Raspberry Pi
                self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            except FileNotFoundError:
                # Ubuntu
                self.arduino = serial.Serial('/dev/ttyS0', 9600, timeout=1)
        except SerialException:
            # Windows
            self.arduino = serial.Serial('com3', 9600, timeout=1)
        sleep(2)  # Must wait 2 seconds for arduino connection to fully initialize
        # Keyboard control support
        self._up = False
        self._down = False
        self._default_speed = default_speed
        # Code control support
        self._forward = False
        self._backward = False
        # Code and Keyboard shared support
        self._left = False
        self._right = False
        self._previous_speed = 0
        self._previous_turn = [0, 0]
    
    def send_instructions(self, speed: int, turn: list):
        # Send [speed, forward boolean, left turn boolean, right turn boolean]
        self.arduino.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))
        return None

    def control(self, code: list):
        """
        :param code: Expected boolean list input for [left, forward, right, backward, speed]
        left: boolean, left key pressed
        forward: boolean, up key pressed
        right: boolean, right key pressed
        backward: boolean, down key pressed
        speed: int, range(0,10) (slow - fast)
        turn: boolean list of 2, [left motor on, right motor on]
        :return: True
        """
        left = code[0]
        forward = code[1]
        right = code[2]
        backward = code[3]
        speed = code[4]
        speed = int(speed / 9.0 * 100)  # Convert to 0 - 90 scale for arduino
        turn = [0, 0]  # Setting default to 0's in case of

        # Calculate instructions and write data to arduino using robot function
        # For conflicting instructions the first signal takes priority
        # Ex. If up is pressed, pressing down does nothing. Etc..
        self._forward = forward if not self._backward else False
        self._backward = backward if not self._forward else False
        self._left = left if not self._right else False
        self._right = right if not self._left else False

        # If either the forward or backward (up or down) keys are pressed
        if self._forward or self._backward:
            # If the left or right keys are pressed
            if self._left or self._right:
                # Swap the values for turns

                turn = [int(not self._left), int(not self._right)]
            if self._backward:
                # Negative speed
                speed *= -1
        elif self._left or self._right:
            turn = [int(not self._left) * 2, int(not self._right) * 2]
        else:
            speed = 0

        # For troubleshooting/development
        # print([abs(speed), speed >= 0, turn[0], turn[1]])

        # If any changes, write new data to arduino
        if self._previous_turn != turn or self._previous_speed != speed:
            self.send_instructions(speed, turn)
            self._previous_turn = turn
            self._previous_speed = speed
        return True
