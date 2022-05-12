from random import randint, random
from ceaser_decrypt import decrypt
from ceaser_encrypt import encrypt

def encrypt_decrypt_string():
    #num_layers=int(random()*(10**randint(1,10)))
    num_layers=randint(0,1000)
    print(num_layers)
    ekeys=list()

    for i in range(num_layers):
        ekeys.append(randint(0,26))

    estring=None
    for key in ekeys:
        estring,curr_key=encrypt(estring,key)
        
    #Encrypted
    print("String: "+estring)#,f"|Keys: {ekeys} {sum(ekeys)}")

    dkeys=ekeys[::-1]
    dstring=estring
    for key in dkeys:
        dstring,curr_key=decrypt(dstring,key)
        
    #Decrypted
    print("String: "+dstring)#,f"|Keys: {dkeys} {sum(dkeys)}")