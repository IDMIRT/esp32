from machine import Pin
from time import sleep

class ErrorTemplateLenght(Exception):
        pass
    
class ErrorLetter(Exception):
    pass


class ShiftRegisterOut:
    
    
    
    def __init__(self, lutch, clock, data, oe=None, mr=None):    
        self.lutch = lutch
        self.clock = clock
        self.data = data
        self.oe= oe
        self.mr = mr
        if self.mr:
            self.mr.on()
            
        
    def clear(self):
        if self.mr:
            self.mr.off()
            self.lutch_turn()
            self.mr.on()
    
    
    def clock_turn(self):
        self.clock.on()
        self.clock.off()
        
    def lutch_turn(self):
        self.lutch.on()
        self.lutch.off()

        
    def send(self, out):
        if type(out)==int:
            self.send_int(out)
        elif type(out)==str:
            self.send_str(out)
            
        
        self.lutch_turn()
            
    def send_to_pin(self, pins_out):
        for value in pins_out:              
                self.data(value)
                self.clock_turn()
        
        
        
    def send_str(self, template):
        arr_to_registr = []
        if len(pattern) > 8:
            raise ErrorTemplateLenght('Шаблон не может быть больше восьми символов')
        elif len(pattern) < 8:
            raise ErrorTemplateLenght('Шаблон не может быть меньше восьми символов')
        
        for count in range(8):
            if pattern[count] in ['0','1']:
                arr_to_registr.append(int(pattern[count]))
            else:
                raise ErrorLetter('В шаблоне можно использовать только 0 и 1')
        self.send_to_pin(arr_to_registr)
    
            
            
        
    
    
    def send_int(self,pin_out):
        arr_to_registr = [1 if x==pin_out else 0 for x in range(8)]
        self.send_to_pin(arr_to_registr)           
        
        
        


clock = Pin(5, Pin.OUT) #shcp
lutch = Pin(4,Pin.OUT)#stcp
data = Pin(2,Pin.OUT)#ds
mr = Pin(15,Pin.OUT)#mr
shift_new = ShiftRegisterOut(lutch, clock,data,mr=mr)
for i in range(8):
    shift_new.send(i)
    sleep(0.5)
    
shift_new.clear()
    
        
    
    
    
    