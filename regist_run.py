from machine import Pin



clock = Pin(5, Pin.OUT) #shcp
lutch = Pin(4,Pin.OUT)#stcp
data = Pin(2,Pin.OUT)#ds
arr_to_registr = [0 if x-1!=2 else 1 for x in range(7)]#[1,0,0,1,0,0,0,1]

def clock_turn():
    clock.on()
    clock.off()


def lutch_turn():
    lutch.on()
    lutch.off()

while True:
    for value in arr_to_registr:
        data(value)
        clock_turn()
    lutch_turn()


