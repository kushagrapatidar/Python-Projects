import winsound

def beep():
    #winsound.Beep(1000//4,1000)
    i=1000
    while 1000<=i<=131068:#131068
        print(i)
        winsound.Beep(i//4,150)
        i=i+4

