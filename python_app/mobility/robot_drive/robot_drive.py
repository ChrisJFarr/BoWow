import keyboard
import serial
import struct
from time import sleep, time
from serial import SerialException


# Create robot drive class
class RobotDrive:
    
    def __init__(self, default_speed=80):
        # Start the serial port to communicate with arduino
        try:
            self.arduino = serial.Serial('/dev/ttyS0', 9600, timeout=1)
        except SerialException:
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
    
    # def execute(plan: string):
        # Take string input

    def actions(self):  # ->
        action_dict = {"f": self.forward,
                       "b": self.backward,
                       "l": self.left,
                       "r": self.right}
        return action_dict
    
    def right(self):
        self.rotateDegrees(90, self._default_speed)
        self.forward()
        return None
    
    def left(self):
        self.rotateDegrees(90, -self._default_speed)
        self.forward()
        return None
    
    def forward(self):
        self.driveDistance(12, self._default_speed)
        return None
    
    def backward(self):
        self.driveDistance(12, -self._default_speed)
        return None
    
    def sendInstructions(self, speed: int, turn: list):
        self.arduino.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))
        return None
    
    def drive(self, seconds: float, speed: int):
        # No turn
        turn = [0, 0]
        #sleep(0)
        # todo Send drive instructions to arduino
        self.sendInstructions(speed, turn)
        # todo Wait seconds
        sleep(seconds)
        # todo Send stop instructions to arduino
        self.sendInstructions(0, turn)
        return None
    
    def driveDistance(self, distance: int, speed: int):
        # distance is in inches
        seconds = distance / (abs(speed) * 0.068)  # Rough conversion to seconds using test data
        self.drive(seconds, speed)
        return None
    
    def rotate(self, seconds: float, speed: int):
        if speed > 0:
            turn = [2, 0]
        else:
            turn = [0, 2]
        self.sendInstructions(abs(speed), turn)
        sleep(seconds)
        self.sendInstructions(0, [0, 0])
        return None
    
    def rotateDegrees(self, degrees: int, speed: int):
        # convert degrees and speed to time
        seconds = degrees / (abs(speed) * .5232)
        self.rotate(seconds, speed)
        return None
        
    def keyboardControl(self, speed=200):

        print("Press 'esc' to stop")

        defaultSpeed = speed
        defaultTurn = [0, 0]
        
        while True:
            speed = defaultSpeed
            turn = defaultTurn
            # Loop to capture key strokes and write date using robot function
            self._up = keyboard.is_pressed("Up") if not self._down else False
            self._down = keyboard.is_pressed("Down") if not self._up else False
            self._left = keyboard.is_pressed("Left") if not self._right else False
            self._right = keyboard.is_pressed("Right") if not self._left else False
            # print([self.up, self.down, self.left, self.right])
            
            if self._up or self._down:
                if self._left or self._right:
                    turn = [int(not self._left), int(not self._right)]
                if self._down:
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
                self.sendInstructions(speed, turn)
                self._previous_turn = turn
                self._previous_speed = speed
            
            if keyboard.is_pressed("esc"):
                break
        
            sleep(.05)

        return True

    def codeControl(self, code: list):
        # TODO parse a list for driving control
        # Expected boolean list input for [left, up, right, down, speed]
        # Or, [left, forward, right, backward, speed]

        left = code[0]
        forward = code[1]
        right = code[2]
        backward = code[3]
        speed = code[4]  # Scale 0 - 9 (fast)
        speed = int(speed / 9.0 * 100)
        turn = [0, 0]  # Setting default if code all 0's

        # Loop to capture key strokes and write date using robot function
        self._forward = forward if not self._backward else False
        self._backward = backward if not self._forward else False
        self._left = left if not self._right else False
        self._right = right if not self._left else False
        # print([self.up, self.down, self.left, self.right])

        if self._forward or self._backward:
            if self._left or self._right:
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
            self.sendInstructions(speed, turn)
            self._previous_turn = turn
            self._previous_speed = speed
        return True
