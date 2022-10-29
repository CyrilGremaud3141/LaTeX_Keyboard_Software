import time
import serial

# sends a string over Uart to the seeed
ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, parity=serial.PARITY_ODD, timeout=1)
def write_to_computer(text):
    counter = 0
    for t in text:
        if counter == 5:
            time.sleep(0.1)
            counter = 0
        ser.write(bytes(t, 'utf-8'))
        counter += 1