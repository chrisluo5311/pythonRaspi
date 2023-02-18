import RPi.GPIO as GPIO

# led燈: gpio17 孔位11
ledLight = 11
# 按鈕: GPIO18 孔位12
button = 12


def setupenv():
    GPIO.setmode(GPIO.BOARD)
    # led輸出 OUT
    GPIO.setup(ledLight, GPIO.OUT)
    # 按鈕輸入，上拉電阻(原理: 按鈕鬆開時高電壓，按下時低電壓)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def execute():
    while True:
        # 按下去接收低電壓
        # GPIO.input: 讀GPIO pin的value, return  0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
        if GPIO.input(button) == GPIO.LOW:
            GPIO.output(ledLight, GPIO.HIGH)
            print('*** 開燈 ***')
        else:
            # 按鈕鬆開
            GPIO.output(ledLight, GPIO.LOW)
            print('關燈')


def cleanup():
    # 關燈
    GPIO.output(ledLight, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    print('按鈕測試開始')
    setupenv()
    try:
        execute()
    except KeyboardInterrupt:
        cleanup()
