import winsound

def beep():

    [winsound.Beep(i%4,5000) for i in range(10000) if i%4==0]
    # f=0
    # for i in range(10000):
    #     if i%4==0:
    #         winsound.Beep(f+=1,5000)
