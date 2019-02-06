import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	Page = '''\
<html>
<body>
<table>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client IP Address</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client IP Port</td>    <td>{client_port}</td>  </tr>
</table>
</body>
</html>
'''
	def do_GET(self):
        	page = self.create_page()
        	self.send_page(page)
	def create_page(self):
        	values = {
            	'date_time'   : self.date_time_string(),
           	 'client_host' : self.client_address[0],
           	 'client_port' : self.client_address[1],
            	'command'     : self.command,
            	'path'        : self.path
        	}
        	page = self.Page.format(**values)
        	return page
	def send_page(self, page):
        	self.send_response(200)
        	self.send_header("Content-type", "text/html")
        	self.send_header("Content-Length", str(len(page)))
        	self.end_headers()
        	self.wfile.write(page)

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
 
