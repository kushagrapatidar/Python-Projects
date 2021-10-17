import pyqrcode
import png

#Read Function
def read(qrname):
    return qrname

#View Function
def view(qrname):
    print(qrname)

#Generate Funtion
def generate(qrname):
    title=input('Enter the title: ')
    print("Enter the Information")
    name=input('Name: ')
    age=input('Age: ')
    contact=input('Contact: ')
    address=input('Address: ')
    linkedin=input('LinkedIn: ')
    social_media=input('Social Media: ')

    data=title+'\n'+'Name: '+name+'\n'+'Age: '+age+'\n'+'Contact: '+contact+'\n'+'Address: '+address+'\n'+'LinkedIn: '+linkedin+'\n'+'Social Media: '+social_media
    url=pyqrcode.create(data)

    url.svg(qrname-'png'+'svg', scale=8)

    url.png(qrname, scale=6)

    return qrname

#Update Function
def update(qrname):
    return(qrname)

#Driver Code
def myqr(qrname=None):
    if qrname==None:
        qrname=input("Enter the name of QR Code with extension: ")
    ch=input("Do you want to generate a new QR Code?\n('Y for Yes and 'N' for No): ")
    if ch.upper()=='Y':
        qrname=generate(qrname)
    else:
        ch=input("Do you want to Update or View the data on your QR Code?\n('U' to Update and 'V' to View the data): ")
        if ch.upper()=='U':
            update(qrname)
        else:
            view(qrname)
    ch=input("Do you want to continue?\n('Y for Yes and 'N' for No): ")
    if ch.upper()=='Y':
        myqr(qrname)
