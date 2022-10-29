import board
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard, Keycode
# from keyboard_layout_win_de import KeyboardLayout
from keyboard_layout_us_dvo import KeyboardLayout




kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

ser = busio.UART(board.TX, board.RX, baudrate=9600, parity=busio.UART.Parity.ODD)

while True:
    data = ser.read(1)
    if data is not None:
        data_string = ''.join([chr(b) for b in data])

        try:
            layout.write(data_string)
        except:
            pass
