# Optimizing serial input to arduino, delimited string
import serial
import struct

arduino = serial.Serial('com3', 9600, timeout=1)
arduino.write("testing:".encode("utf-8"))




