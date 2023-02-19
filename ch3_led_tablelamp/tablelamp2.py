"""
gpiozero 文檔: https://gpiozero.readthedocs.io/en/stable/

"""
from gpiozero import LED, Button
from signal import pause

print('按鈕測試開始')

led = LED(17)
button = Button(18)

button.when_pressed = led.on
button.when_released = led.off

pause()
