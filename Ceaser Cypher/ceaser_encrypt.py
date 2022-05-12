def get_encrypt(string,key=None):
    alphacap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphasmall="abcdefghijklmnopqrstuvwxyz"
    if key==None:
        key=int(input('Enter the Key: '))
    new_alphacap=alphacap[-(key):]+alphacap[:-(key)]
    new_alphasmall=alphasmall[-(key):]+alphasmall[:-(key)]
    new_str=""
    for i in range(len(string)):
        if string[i] in alphacap:
            new_str+=new_alphacap[alphacap.index(string[i])]
        elif string[i] in alphasmall:
            new_str+=new_alphasmall[alphasmall.index(string[i])]
        else:
            new_str+=string[i]
    return new_str,key

def encrypt(string=None,key=None):
    if string==None:
        string=input('Enter the Text: ')
    string,key=get_encrypt(string,key)
    return string,key