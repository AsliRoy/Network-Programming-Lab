import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	# Get the size of the socket's send buffer
	bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Buffer size [Before]:%d" %bufsize
	sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)

	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_SNDBUF,
		SEND_BUF_SIZE)
	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_RCVBUF,
		RECV_BUF_SIZE)

	bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Buffer size [After]:%d" %bufsize

def test_socket_modes():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setblocking(1)
	s.settimeout(0.5)
	s.bind(("127.0.0.1", 0))
	socket_address = s.getsockname()
	print "Trivial Server launched on socket: %s" %str(socket_address)
	while(1):
		s.listen(1)
if __name__ == '__main__':
	modify_buff_size()
	test_socket_modes()
