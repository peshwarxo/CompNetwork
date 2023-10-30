import Lsbpro2
import socket    #Import socket module
#import pickle

s = socket.socket()     # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
#s.send("Hello server!".encode())
msg=input("Enter message to encrypt :")     #getting message>.!
Lsbpro2.encrypt('tosend.jpg',msg)           #encrypting message..!!
lisi=Lsbpro2.getList()                      #dumping the list
data=str(lisi)
s.send(data.encode())
f = open('torecv.png', 'rb')                #sending list       #getting list
print('Sending...')
l = f.read(1024)
while (l):
    #print('Sending...')
    lst=Lsbpro2.getList()
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close         # Close the socket when done





