# Здесь я выкладываются небольшие библиотеки  для работы с устройствами подключаемыми к ESP32.

# reg_74hc595
Небольшой класс на micropython для работы с микросхемой 74hc595 подключенной к ESP32.
![Входы выходы на микросхеме](https://github.com/IDMIRT/esp32/blob/master/picture/74hc595-serial-shift-register.jpg)
|Контакты| Описание |
|-----|---------------------------------------------|
| VCC | Питание 3 или 5 вольт                       |
| GND | Земля                                       | 
|Q0-Q7| Выходные контакты они же выводы или пины    |
| DS  | Входной контакт для передачи битов в регистр|
|SHCP | Контакт синхронизации при подаче питания передает бит из ds в память регистра   |
|STCP |Контакт передачи, при подаче питания передает питания на пины согласно данными в DS|
| MR  |Контакт сброса, при подаче питания сбрасывает все значения Q0-Q7 на 0|
| OE  | При подаче питания отключет все выводы в микросхеме        |
| Q7S | Контакт связи с другой микросхемой 74hc595  |


![Схема подключения к контроллеру](https://github.com/IDMIRT/esp32/blob/master/picture/595_single.png)

##Пример кода с использванием класса
```python
from machine import Pin
from time import sleep
from reg_74hc595 import ShiftRegisterOut

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



