from machine import Pin
from time import sleep


class ErrorTemplateLenght(Exception):
    pass


class ErrorLetter(Exception):
    pass


class ShiftRegisterOut:
    """
    Простой класс для работы с регистром сдвига исходящим 74рс595 в ESP32 и Raspberry
    при инициализации  обязательные параметры:
    lutch - тактовый вход регистра хранения ST_CP устанавливает из памяти data(ds)
    clock - тактовый вход регистра сдвига SH_CP помещает данные в память регистра
    data - вход последовательных данных 8 бит сюда заносим побитово данные (0,1)
    необязательные параметры:
    mr - очистка регистра памяти при если не нужен подключаем на питание
    oe - отключение всех выводов регистра если не нужен подключаем на 0
    С помощью класса можно работать как с единичным входом send_int так  и c помощью шаблона send_str
    """

    def __init__(self, lutch, clock, data, oe=None, mr=None):
        self.lutch = lutch
        self.clock = clock
        self.data = data
        self.oe = oe
        self.mr = mr
        if self.mr:
            self.mr.on()
        if self.oe:
            self.oe.off()

    def pin_off(self):
        if self.oe:
            self.oe.on()

    def pin_on(self):
        if self.oe:
            self.oe.off()

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
        if type(out) == int:
            self.send_int(out)
        elif type(out) == str:
            self.send_str(out)

        self.lutch_turn()

    def send_to_pin(self, pins_out):
        for value in pins_out:
            self.data(value)
            self.clock_turn()

    def send_str(self, template):
        arr_to_register = []
        if len(template) > 8:
            raise ErrorTemplateLenght('Шаблон не может быть больше восьми символов')
        elif len(template) < 8:
            raise ErrorTemplateLenght('Шаблон не может быть меньше восьми символов')

        for count in range(8):
            if template[count] in ['0', '1']:
                arr_to_register.append(int(template[count]))
            else:
                raise ErrorLetter('В шаблоне можно использовать только 0 и 1')
        self.send_to_pin(arr_to_register)

    def send_int(self, pin_out):
        """
        Формирует маску для помещение в память и включения одного пина
        :param pin_out: номер Q0-Q7 который нужно включить
        :return: маска(список) который будет помещаться в регистр памяти
        можно упростить используя побитовые операции (x>>1)&1 и range(pin_out) для экономии
        но тогда не забываем про очистку перед началом передачи данных self.clear() и обязательно
        подключаем mr на пин
        """
        arr_to_register = []
        if mr:
            self.clear()
            arr_to_register = [(x>>1)&1 for x in range(pin_out)]
        else:
            arr_to_register = [1 if x == pin_out else 0 for x in range(8)]

        self.send_to_pin(arr_to_register)


clock = Pin(5, Pin.OUT)  # shcp
lutch = Pin(4, Pin.OUT)  # stcp
data = Pin(2, Pin.OUT)  # ds
mr = Pin(15, Pin.OUT)  # mr
shift_new = ShiftRegisterOut(lutch, clock, data, mr=mr)
for i in range(8):
    shift_new.send(i)
    sleep(0.5)

shift_new.clear()
