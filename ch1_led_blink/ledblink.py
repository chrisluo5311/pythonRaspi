import RPi.GPIO as GPIO
import time

"""
全域變數GPIO.BOARD: 
使用led output的實際孔位
GPIO17為第11孔位
-----
若使用GPIO.BCM:
則是pin serial number based on CPU of BCM chip.
GPIO17
"""
ledlight = 11


def setupenv():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledlight, GPIO.OUT, GPIO.LOW)
    # GPIO.output(ledlight,GPIO.LOW) # 後面State可以是 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
    print('初始設定完畢，led孔位:%d' % ledlight)


def execute():
    while True:
        GPIO.output(ledlight, GPIO.HIGH)
        print('-- led 發亮 --')
        GPIO.output(ledlight, GPIO.LOW)
        print('關燈')
        time.sleep(1)  # 間隔


def cleanupled():
    GPIO.cleanup()


if __name__ == '__main__':
    print('***led亮燈測試開始***')
    setupenv()
    try:
        execute()
    except KeyboardInterrupt:
        # ctrl-c中止
        cleanupled()
