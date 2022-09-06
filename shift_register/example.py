from machine import Pin
from time import sleep
from shift_register_out import ShiftRegisterOut

clock = Pin(5, Pin.OUT)  # shcp
lutch = Pin(4, Pin.OUT)  # stcp
data = Pin(2, Pin.OUT)  # ds
mr = Pin(15, Pin.OUT)  # mr
shift_new = ShiftRegisterOut(lutch, clock, data, mr=mr)

for i in range(8):
    shift_new.send(i)
    sleep(0.5)

shift_new.clear()

register_templates = ['00011000','00111100', '01111110', '11111111',
                      '00000000','10000000','11000000','11100000','11110000',
                      '11111000','11111100','11111110','11111111']

for value in register_templates:
    shift_new.send(value)
    sleep(0.5)
