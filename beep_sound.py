import winsound

def beep():
    #winsound.Beep(1000//4,1000)
    i=1000
    while 1000>=i>=1500:#131069
        if i%4==0:
            print(i//4)
            winsound.Beep(i//4,100)
            i=i+4

