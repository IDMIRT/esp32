


class ShiftRegisterOut:
    """
    Простой класс для работы с регистром сдвига исходящим 74hc595 в ESP32 и Raspberry
    при инициализации  обязательные параметры:
    latch - тактовый вход регистра хранения ST_CP устанавливает из памяти data(ds) на выводы
    clock - тактовый вход регистра сдвига SH_CP помещает данные в память регистра
    data - вход последовательных данных 8 бит сюда заносим побитово данные (0,1)
    необязательные параметры:
    mr - очистка регистра памяти если не нужен подключаем на питание
    oe - отключение всех выводов регистра если не нужен подключаем на 0
    register_count - при использовании нескольких регистров через Q7S указываем количество регистров по умолчанию 1
    С помощью класса можно работать как с единичным выходом  _send_int так и c помощью шаблона _send_str
    """

    def __init__(self, latch, clock, data, oe=None, mr=None, register_count=1):
        self.latch = latch
        self.clock = clock
        self.data = data
        self.oe = oe
        self.mr = mr
        self.register_count = register_count
        if self.mr:
            self.mr.on()
        if self.oe:
            self.oe.off()

    def pins_off(self):
        if self.oe:
            self.oe.on()

    def pins_on(self):
        if self.oe:
            self.oe.off()

    def clear(self):
        if self.mr:
            self.mr.off()
            self._lutch_turn()
            self.mr.on()

    def _clock_turn(self):
        self.clock.on()
        self.clock.off()

    def _lutch_turn(self):
        self.latch.on()
        self.latch.off()

    def send(self, in_data):
        if type(in_data) == int:
            self._send_int(in_data)
        elif type(in_data) == str:
            self._send_str(in_data)
        else:
            raise TypeError('Неверный тип данных для передачи в регистр')

        self._lutch_turn()

    def _send_to_pin(self, pins_out):
        for value in pins_out:
            self.data(value)
            self._clock_turn()

    def _send_str(self, template):
        """
        Процедура формирующая из строки шаблона список для передачи в память регистра
        :param template: шаблон строки для вывода в пины Q0-Qn шаблон состоит из чисел в строковой
        переменной типа '10000000' ноль не работающий пин 1 работающий
        :return: список вывода на пины типа [1,0,0,0,0,0,0,0]
        """
        arr_to_register = []
        if len(template) > 8*self.register_count:
            raise IndexError('Шаблон не содержать количество символов больше количества выводов')
        elif len(template) < 8*self.register_count:
            raise IndexError('Шаблон не может содержать количество символов меньше количества выводов')

        for count in range(8*self.register_count):
            if template[count] in ['0', '1']:
                arr_to_register.append(int(template[count]))
            else:
                raise SyntaxError('В шаблоне можно использовать только 0 и 1')
        self._send_to_pin(arr_to_register)

    def _send_int(self, pin_out):
        """
        Формирует маску для помещение в память и включения одного пина
        :param pin_out: номер Q0-Qn который нужно включить
        :return: маска(список) который будет помещаться в регистр памяти

        """
        if pin_out > 7*self.register_count:
            raise IndexError('Номер пина не может быть больше  количества выводов')


        arr_to_register = [1 if x == pin_out else 0 for x in range(8 * self.register_count)]

        self._send_to_pin(arr_to_register)

