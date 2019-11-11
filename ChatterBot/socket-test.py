# Echo server program
import socket

def changeString(myString):
    newString = myString + " - CHANGED\r\n"

    return newString

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9876              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    data = conn.recv(1024)
    decodedRequest = data.decode("utf-8")
    print( decodedRequest )
    if not data: break
    conn.sendall(str.encode(changeString(decodedRequest))) # turn it back into bytes 
conn.close()

