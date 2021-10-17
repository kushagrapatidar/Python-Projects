import pyqrcode
import png

#Read Function
def read(qr):
    return qr

#View Function
def view(qr):
    print(qr)

#Generate Funtion
def generate():
    print("Enter the Information")
    name=input('Name: ')
    dob=input('DOB (DD/MM/YYYY): ')
    highest_qualifications=input('Highest Qualifications: ')
    contact=input('Contact')
    

    data=name+'\n'+dob+'\n'+highest_qualifications+'\n'+contact
    url=pyqrcode.create(data)

    url.svg("Personal Info.svg", scale=8)

    url.png('Personal Info.png', scale=6)
    qr='Personal Info.png'
    return qr

#Update Function
def update(qr):
    return(qr)

#Driver Code
def myqr(qrname=None):
    ch=input("Do you want to generate a new QR Code?\n('Y for Yes and 'N' for No): ")
    if ch.upper()=='Y':
        qrname=generate()
    else:
        if qrname==None:
            qrname=input("Enter the name of QR Code with extension: ")
        ch=input("Do you want to Update or View the data on your QR Code?\n('U' to Update and 'V' to View the data): ")
        if ch.upper()=='U':
            update(qrname)
        else:
            view(qrname)
    ch=input("Do you want to continue?\n('Y for Yes and 'N' for No): ")
    if ch.upper()=='Y':
        myqr(qrname)
