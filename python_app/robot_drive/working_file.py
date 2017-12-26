## Standardizing movement of robot to a finite set of functions
## Rotate: int input for degrees to turn
## Drive: boolean forward input for direction and int distance for inches to drive


# todo Syncing commands with robot_drive (permanent version of robot drive arduino code)
# todo On initizializing, set default speed with
# data.write(struct.pack('>B', default_speed))

# todo Drive robot forward for x seconds and measure distance traveled
# Full speed
# Half speed

# todo Rotate robot for x seconds and calculate degrees rotated
# todo change speed and calculate again, try to predict movement for any speed assuming linear variations



# Use keyboard control for driving robot
# import serial
# Linux
import keyboard
import serial
import struct
from time import sleep, time
import argparse

# Arduino input details:
# struct.pack('>BBBB', speed, direction, turn[0], turn[1])
# int speed: int of range(0, 256), determines current driving speed for forward or reverse
# boolean direction: True drives forward, False drives backward
# int list turn: 0, 1, or 2
# when [0, 1], left turn while driving forward
# [1, 0] right turn while driving forward
# [0, 2] left spin, not driving
# [2, 0] right spin, not driving

# Driving input information
# If up, then positive speed
# If down, then negative speed
# If neither, then 0 speed and 1 direction

# If non-zero speed and left then turn = [0, 1]
# If zero speed and left then turn = [0, 2]
# If non-zero speed and right then turn = [1, 0]
# If zero speed and right then turn = [2, 0]
# test


# Create robot drive class
class RobotDrive:
    
    def __init__(self):
        # Start the serial port to communicate with arduino
        self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        # Keyboard control support
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.previous_speed = 0
        self.previous_turn = [0, 0]
    
    def driveStraight(self, seconds: int):
        start_time = time()
        #while time() - start_time < 3:
    
    def keyboardControl(self, speed = 200):
        defaultSpeed = speed
        defaultTurn = [0, 0]
        while True:
            speed = defaultSpeed
            turn = defaultTurn
            # Loop to capture key strokes and write date using robot function
            self.up = keyboard.is_pressed("Up") if not self.down else False
            self.down = keyboard.is_pressed("Down") if not self.up else False
            self.left = keyboard.is_pressed("Left") if not self.right else False
            self.right = keyboard.is_pressed("Right") if not self.left else False
            print([self.up, self.down, self.left, self.right])
            
            if self.up or self.down:
                if self.left or self.right:
                    turn = [int(not self.left), int(not self.right)]
                if self.down:
                    # Negative speed
                    speed *= -1
            elif self.left or self.right:
                turn = [int(not self.left) * 2, int(not self.right) * 2]
            else:
                speed = 0
            
            # For troubleshooting/development
            print([abs(speed), speed >= 0, turn[0], turn[1]])
        
            # If any changes, write new data to arduino
            if self.previous_turn != turn or self.previous_speed != speed:
                self.arduino.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))
                self.previous_turn = turn
                self.previous_speed = speed
            
            if keyboard.is_pressed("esc"):
                break
        
            sleep(.05)

        return True


if __name__ == "__main__":
    
    rd = RobotDrive()
    rd.keyboardControl()







