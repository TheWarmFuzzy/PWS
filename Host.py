import socket
import StringIO
import sys

class WSGIServer(object):
	
	address_family = socket.AF_INET
	socket_type = socket.SOCK_STREAM
	request_queue_size = 1
	
	def __init__(self, address):
		#Create listening socket
		self.listen_socket = listen_socket = socket.socket(self.address_family, self.socket_type)
		
		listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		listen_socket.bind(address)
		
		listen_socket.listen(self.request_queue_size)
		
		host, port, self.listen_socket.getsockname()[:2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port
		self.headers_set = []
	
	def set_app(self, application):
		self.application = application
		
	def serve_forever(self):
		listen_socket = self.listen_socket
		while True:
			self.client_connection, client_address = listen_socket.accept()
			
			self.handle_one_request()
			
	def handle_one_request(self):
		