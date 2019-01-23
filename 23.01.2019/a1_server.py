import socket
import time
host = socket.gethostname() 
port = 12346              
socksize = 1024
s = socket.socket()
s.bind((host, port))        
print(" The server started on port: %s" %port)
s.listen(1)
print("The server is now listening for potential clients->->->")
while True:
	c, addr = s.accept()
	print 'New client connection accepted from %s:%d' % (addr[0], addr[1])
	c.settimeout(10)	
	c.send('Sending back your IP address : {}'.format(addr))
	
	try:
		data = c.recv(socksize)
		if data == 'QUIT':
			c.send('Quitting the connection now')
			print ("Connection has been terminated by the client.")
			c.close()
		elif data == 'IP':
			c.send('Your IP address : {}'.format(addr))
		elif data == 'TIME':
			localtime = time.asctime( time.localtime(time.time()) )
			t = localtime
			c.send('Current time is : {}'.format(t))
	except socket.timeout:
		print ("10 second timeout, please retry again")
		c.send('timeout')
		c.close()
