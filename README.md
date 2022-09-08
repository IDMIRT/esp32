# Здесь я выкладываются небольшие библиотеки  для работы с устройствами подключаемыми к ESP32.

# reg_74hc595
Небольшой класс на micropython для работы с микросхемой 74hc595 подключенной к ESP32.
![Входы выходы на микросхеме](https://github.com/IDMIRT/esp32/blob/master/picture/74hc595-serial-shift-register.jpg)

|Q0-Q7| Выходные контакты они же выводы или пины    |
|-----|---------------------------------------------|
| DS  | Входной контакт для передачи битов в регистр|
|SHCP | Контакт синхронизации при подаче питания передает бит из ds в память регистра   |
|STCP |Контакт передачи, при подаче питания передает питания на пины согласно данными в DS|
| MR  |Контакт сброса, при подаче питания сбрасывает все значения Q0-Q7 на 0|
| OE  | При подаче питания отключет все выводы в микросхеме        |
| Q7S | Контакт связи с другой микросхемой 74hc595  |


![Схема подключения к контроллеру](https://github.com/IDMIRT/esp32/blob/master/picture/ShftOut_Schema2.gif)



