# Use keyboard control for driving robot
# import serial
# Linux
import keyboard
import serial
import struct
from time import sleep

# Start the serial port to communicate with arduino
data = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# todo Turns should add a bit to one side and remove a bit from the other
# todo Speed should be a constant level
# todo Robot should stop when no buttons are pressed
# todo Fix the turning inversion while driving
left = False
up = False
right = False
down = False

previous_turn = [0, 0]
previous_speed = 200

def manageRobot():
    global previous_turn
    global previous_speed
    speed = 200
    turn = [0, 0]

    if up:
        speed *= 1
    elif down:
        speed *= -1
    else:
        speed *= 0

    if left:
        turn = [0, 1] if speed else [0, 2]
    elif right:
        turn = [1, 0] if speed else [2, 0]
    # print([abs(speed), speed >= 0, turn[0], turn[1]])
    if previous_turn != turn or previous_speed != speed:
        data.write(struct.pack('>BBBB', abs(speed), speed >= 0, turn[0], turn[1]))
        previous_turn = turn
        previous_speed = speed
    

    return True

if __name__ == "__main__":

    while True:
        # Loop to capture key strokes and write date using robot function
        up = keyboard.is_pressed("Up") if not down else False
        down = keyboard.is_pressed("Down") if not up else False
        left = keyboard.is_pressed("Left") if not right else False
        right = keyboard.is_pressed("Right") if not left else False
        # print([up, down, left, right])
        
        manageRobot()
        
        if keyboard.is_pressed("esc"):
            break
        
        sleep(.1)


# If up, then positive speed
# If down, then negative speed
# If neither, then 0 speed and 1 direction

# If non-zero speed and left then turn = [0, 1]
# If zero speed and left then turn = [0, 2]
# If non-zero speed and right then turn = [1, 0]
# If zero speed and right then turn = [2, 0]

