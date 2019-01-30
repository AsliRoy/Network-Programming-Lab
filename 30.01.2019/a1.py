
import socket 

def get_Host_name_IP(): 
	try: 
		host_name = socket.gethostname() 
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		print("IPv4 Address : ",s.getsockname()[0])
		print("Machine name : ",host_name)  
	except: 
		print("Unable to get Hostname and IP") 





get_Host_name_IP()


