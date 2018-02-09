import requests
import keyboard
from time import sleep

if __name__ == "__main__":

    # ip = "192.168.56.1"  # Windows as server ip
    ip = "192.168.1.201"  # Pi as server ip
    port = "5000"
    speed = 7
    prev_code = [0, 0, 0, 0, 0]  # Global variable for tracking changes

    # keyboard application that hits api with any changes
    while True:
        up = int(keyboard.is_pressed("Up"))
        down = int(keyboard.is_pressed("Down"))
        left = int(keyboard.is_pressed("Left"))
        right = int(keyboard.is_pressed("Right"))

        code = [left, up, right, down, speed]

        if code != prev_code:
            url = "http://%s:%s/drive/" % (ip, port)
            try:
                requests.get(url=url + "".join([str(c) for c in code]))
            except Exception as e:
                raise e
            prev_code = code

        if keyboard.is_pressed("esc"):
            break

        sleep(.05)
