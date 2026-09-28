import time
import datetime
import tm1637

Display = tm1637.TM1637(clk=23, dio=24)

Display.write([0, 0, 0, 0])
Display.brightness(1)

while True:
    now = datetime.datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    show_colon = (second % 2 == 0)

    Display.numbers(hour, minute, colon=show_colon)

    time.sleep(1)
