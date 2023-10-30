import Lsbpro2
#import pickle
import socket # Import socket module

s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
f = open('torecv.jpg', 'wb')

s.listen(5) # Now wait for client connection.


while True:
    c, addr = s.accept()    # Establish connection with client.
    print('Got connection from ', addr)
    print("Receiving...")
    dat=c.recv(4096)
    dat=dat.decode('utf-8')
    dat=eval(dat)
    l = c.recv(1024)
    while (l):
        #print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    c.send('Thank you for connecting'.encode())
    strr=Lsbpro2.decrypt('torecv.jpg',dat)
    print("Encrypted Message is :"+strr)
    #print(Lsbpro2.decrypt('torecv.jpg',dat))
    c.close()   # Close the connection
    break


