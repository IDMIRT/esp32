from machine import Pin

class ShiftRegisterOut:

    def __init__(self, lutch, clock, data):
        self.lutch = lutch
        self.clock = clock
        self.data = data


    def clock_turn():
        clock.on()
        clock.off()

    def lutch_turn():
        lutch.on()
        lutch.off()


    def send(self):
        arr_to_registr = [1,0,0,1,0,0,0,1]
        for value in arr_to_registr:
            self.data(value)
            self.clock_turn()
        self.lutch_turn()



clock = Pin(5, Pin.OUT) #shcp
lutch = Pin(4,Pin.OUT)#stcp
data = Pin(2,Pin.OUT)#ds

shift_new = ShiftRegisterOut(lutch, clock,data)
shift_new.send()







