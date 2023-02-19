"""
gpiozero 文檔: https://gpiozero.readthedocs.io/en/stable/

"""
from gpiozero import LED, Button
from signal import pause

print('按鈕測試開始')

led = LED(17)
button = Button(18)


def onButtonPressed():
    led.toggle()  # 如果是亮著的就關閉，如果是關燈狀態則開啟
    if led.is_lit:
        print("Led turned on >>>")
    else:
        print("Led turned off <<<")


button.when_pressed = onButtonPressed

pause()
