

class ShiftRegister:

    def __init__(self, latch, clock, data, oe=None, mr=None):
        self.data = data
        self.clock = clock
        self.latch = latch
        self.oe = oe
        self.mr = mr


    def send(self, pin_out):
        if type(pin_out)==int:
            self.send_bits(self._int_pin(pin_out))
        elif type(pin_out)==str:
            self.send_bits(self._str_pin(pin_out))
        # elif type(pin_out)==list:
        #     pass


    def send_bits(self, bit_send):
        for value in bit_send:
            self.data = value
            self._clock_turn()
        self._latch_turn()



    def _int_pin(self,pin_out:int):
        out_ports = [1 if x == pin_out else 0 for x in range(7)]
        return out_ports


    def _str_pin(self, pin_out:str):
        out_ports = []
        if len(pin_out) == 8:
            for value in pin_out:
                if value.isnumeric():
                    out_ports.append(int(value))
        elif len(pin_out) < 8:
            for i in range(7):
                if i+1<=len(pin_out):
                    if pin_out[i].isnumeric():
                        out_ports.append(int(pin_out[i]))
                else:
                    out_ports.append(0)
        return out_ports





    def _send_int_pin(self, pin_out):
        pass

    def send_char(self,pin_out):
        pass


    def _oe_trun(self):
        pass

    def _mr_turn(self):
        pass

    def _clock_turn(self):
        self.clock(1)
        self.clock(0)

    def _latch_turn(self):
        self.latch(1)
        self.latch(0)



def return_choose(first_value=0, second_value=7):
    result_out = []

    for i in range(8):
        if i >= first_value and  i <=second_value:
            result_out.append(1)
        else:
            result_out.append(0)

    return result_out

print(return_choose(first_value=3, second_value=6))