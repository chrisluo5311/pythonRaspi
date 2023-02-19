import RPi.GPIO as GPIO

ledLight = 11
buttonNum = 12
outputValue = False


def setenv():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledLight, GPIO.OUT)
    GPIO.setup(buttonNum, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def execute_callback(channel):
    global outputValue
    outputValue = not outputValue
    print('按鈕channel:%d' % channel)
    if outputValue:
        print('*** 亮燈 ***')
    else:
        print('關燈')
    GPIO.output(ledLight, outputValue)


def loop():
    GPIO.add_event_detect(buttonNum, GPIO.FALLING, callback=execute_callback, bouncetime=300)
    while True:
        pass


def cleanup():
    GPIO.cleanup()


if __name__ == '__main__':
    print('*** 桌燈測試開始 ***')
    setenv()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
