import RPi.GPIO as GPIO
import time
import threading

ledPin = [37,35,32,33,18,40,22,38]      
buttonPin = 36  
ledState = 0

def setup():    
    GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for led in ledPin:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)

def buttonEvent(channel):
    global ledState
    ledState = (ledState + 1) % 6
    if ledState == 0:
        ledState = ledState + 1
    print('buttonEvent: ',ledState)

    
def handleButton():
    #Button detect 
    GPIO.add_event_detect(buttonPin,GPIO.FALLING,callback = buttonEvent,bouncetime=300)
    while True:
        time.sleep(0.01)

# Light up an LED every 1 second, a total of 8 LEDs take turns. 
def event1():
    #time.sleep(0.4)
    global ledState
    while True:
        if ledState == 1:
            for led in ledPin:
                print('event1')
                GPIO.output(led, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led, GPIO.LOW)
                if ledState!= 1:
                    print('event1 break')
                    break


# When the Button on the development board is pressed, 
# two LEDs will light up at the same time every 1 second.
def event2():
    #time.sleep(0.4)
    global ledState
    while True:
        if ledState == 2:
            while True:
                print('event2')
                GPIO.output((22,38), GPIO.HIGH)
                time.sleep(1)
                GPIO.output((22,38), GPIO.LOW)
                time.sleep(1)
                if ledState != 2:
                    print('event2 break')
                    break

# After pressing the Button on the development board again, 
# one LED will light up every 1 second 
# and one LED will light up every 0.5 seconds (simultaneously). 
def event3():
    #time.sleep(0.4)
    global ledState    
    while True:
        if ledState == 3:
            print('event3')
            while True:
                new_t = threading.Thread(target=halfSecond)
                new_t.start()
                GPIO.output(35, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(35, GPIO.LOW)
                time.sleep(1)
                if ledState != 3:
                    print('event3 break')
                    break
            
def halfSecond():
    global ledState
    while True:
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(37,GPIO.LOW)
        time.sleep(0.5)
        if ledState != 3:
            print('halfSecond break')
            break

#  After pressing the Button once, all LED lights will flash. 
def event4():
    #time.sleep(0.4)
    global ledState
    while True:
        if ledState == 4:
            print('event4')
            while True:
                ledPin = (37,35,32,33,18,40,22,38)
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(1)
                if ledState!= 4:
                    print('event4 break')
                    break

# Finally press the Button again to return to the state of lighting up an LED every 1 second.
def event5():
    #time.sleep(0.4)
    global ledState
    while True:
        if ledState == 5:
            for led in ledPin:
                print('event5')
                GPIO.output(led, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led, GPIO.LOW)
                if ledState!= 5:
                    print('event5 break')
                    break

def turnoff_all_lights():
    for led in ledPin:
        GPIO.output(led, GPIO.LOW)

def destroy():
    turnoff_all_lights()
    GPIO.cleanup()                     

if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        t = threading.Thread(target=handleButton)
        t.start()
        t1 = threading.Thread(target=event1)
        t1.start()
        t2 = threading.Thread(target=event2)
        t2.start()
        t3 = threading.Thread(target=event3)
        t3.start()
        t4 = threading.Thread(target=event4)
        t4.start()
        t5 = threading.Thread(target=event5)
        t5.start()
    except KeyboardInterrupt:  
        destroy()
        

