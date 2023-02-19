ledState = False

def testfunc():
    global ledState
    ledState = not ledState
    print(ledState)

if __name__ == '__main__':
    testfunc()