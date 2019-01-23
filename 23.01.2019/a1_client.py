import socket,sys              

s = socket.socket()         
host = socket.gethostname() 
port = 12346              

s.connect((host, port))
print s.recv(1024)
shell = sys.stdin.readline().strip()
s.send(shell)
data = s.recv(1024)
output = data
print 'Received', repr(data)

s.close()   
