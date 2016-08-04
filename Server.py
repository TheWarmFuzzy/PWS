from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = '127.0.0.1'
PORT = 80

class RequestHandler(BaseHTTPRequestHandler):
	
	def do_HEAD(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		
	def do_GET(self):
		message = "Hello world!"
		
		self.wfile.write(bytes(message, "utf8"))
		return
	
	def do_POST(self):
		pass
		
def run():
	print("Starting server...")
	
	server_address = (HOST, PORT)
	httpd = HTTPServer(server_address, RequestHandler)
	print('Running server...')
	httpd.serve_forever()

if __name__ == '__main__':
	run()