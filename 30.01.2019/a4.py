import socket

protocol_name = 'tcp'
for port in [80,25,53]:
	print "Port ",port," =>> Service Name: ",socket.getservbyport(port,protocol_name)
