from http.server import HTTPServer, BaseHTTPRequestHandler
from time import strftime
from Lib import mimetypes

class CS2610Assn1(BaseHTTPRequestHandler):

    def serve_file(self, fname):
        try:
            # Opening the file
            f = open(fname, 'rb')
            data = f.read()
            f.close()

            # Serving the header
            self.wfile.write(bytes('HTTP/1.1 200 Ok\n','utf-8'))
            self.wfile.write(bytes("Server: Jack's Private Server\n",'utf-8'))
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
            self.wfile.write(bytes('Connection: close','utf-8'))
            self.wfile.write(bytes(f'Cache-Control: max-age=<{20}>\n','utf-8'))
            self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
            self.send_header(bytes('Content Type','utf-8'),mimetypes.guess_type(fname))
            self.wfile.write(bytes("\n", 'utf-8'))
            # Serving the actual file
            self.wfile.write(data)
        except:
            self.redir5xx()



    def redir301(self, location):
        try:
            # Basically just the necessary stuff for a heading
            print("served 301",location)
            self.wfile.write(b'HTTP/1.1 301 Moved Permanently\n')
            self.wfile.write(b"Server: Jack's Private Server\n")
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
            self.wfile.write(bytes(f"Location: {location}\n", 'utf-8'))
            self.wfile.write(bytes("\n", 'utf-8'))
        except:
            self.redir5xx()

    def redir403(self):
        try:
            # Opening the file
            f = open('forbidden.html', 'rb')
            data = f.read()
            f.close()

            # Serving the header
            self.wfile.write(bytes('HTTP/1.1 403 Forbidden\n', 'utf-8'))
            self.wfile.write(bytes("Server: Jack's Private Server\n", 'utf-8'))
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
            self.wfile.write(bytes('Connection: close\n', 'utf-8'))
            self.wfile.write(bytes(f'Cache-Control: max-age=<{20}>\n', 'utf-8'))
            self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
            self.send_header(bytes('Content Type', 'utf-8'), mimetypes.guess_type('/forbidden.html'))
            self.wfile.write(bytes("\n", 'utf-8'))
            # Serving the actual file
            self.wfile.write(data)
        except:
            self.redir5xx()

    def redir404(self):
        try:
            # Opening the file
            f = open('not found.html', 'rb')
            data = f.read()
            f.close()

            # Serving the header
            self.wfile.write(bytes('HTTP/1.1 404 Not Found\n', 'utf-8'))
            self.wfile.write(bytes("Server: Jack's Private Server\n", 'utf-8'))
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
            self.wfile.write(bytes('Connection: close\n', 'utf-8'))
            self.wfile.write(bytes(f'Cache-Control: max-age=<{20}>\n', 'utf-8'))
            self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
            self.send_header(bytes('Content Type', 'utf-8'), mimetypes.guess_type('/not found.html'))
            self.wfile.write(bytes("\n", 'utf-8'))
            # Serving the actual file
            self.wfile.write(data)
        except:
            self.redir5xx()

    def redir418(self):
        try:
            # Opening the file
            f = open('teapot.html', 'rb')
            data = f.read()
            f.close()

            # Serving the header
            self.wfile.write(bytes('HTTP/1.1 418 teapot\n', 'utf-8'))
            self.wfile.write(bytes("Server: Jack's Private Server\n", 'utf-8'))
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
            self.wfile.write(bytes('Connection: close\n', 'utf-8'))
            self.wfile.write(bytes(f'Cache-Control: max-age=<{20}>\n', 'utf-8'))
            self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
            self.send_header(bytes('Content Type', 'utf-8'), mimetypes.guess_type('/teapot.html'))
            self.wfile.write(bytes("\n", 'utf-8'))
            # Serving the actual file
            self.wfile.write(data)
        except:
            self.redir5xx()

    def redir5xx(self):
        print('in 500')
        # Opening the file
        f = open('not found.html', 'rb')
        data = f.read()
        f.close()

        # Serving the header
        self.wfile.write(bytes('HTTP/1.1 500 Internal Server Error\n', 'utf-8'))
        self.wfile.write(bytes("Server: Jack's Private Server\n", 'utf-8'))
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes('Connection: close\n', 'utf-8'))
        self.wfile.write(bytes(f'Cache-Control: max-age=<{20}>\n', 'utf-8'))
        self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
        self.send_header(bytes('Content Type', 'utf-8'), mimetypes.guess_type('/error.html'))
        self.wfile.write(bytes("\n", 'utf-8'))
        # Serving the actual file
        self.wfile.write(data)


    def redir_debug(self,location):
        response = b'''
HTTP/1.1 200 Ok
Server: Jack's Private Server
Date: '''+ bytes(f'{strftime("%c")}\n','utf-8') + b'''
        
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>DEBUG</title>
</head>
<body>

<h1>--FOR DEBUGGING--</h1>

<p>Server Version: Jack's Private Server</p>
<p>Date and time: '''+ bytes(f'{strftime("%c")}\n','utf-8') + '''</p>
<p>IP address and port: '''+ bytes(f'{self.client_address}\n','utf-8') +''' </p>
<p>Path requested: '''+ bytes(f'{location}\n','utf-8') +''' </p>
<p>HTTP request type: '''+ bytes(f'{self.command}\n','utf-8') +'''</p>
<p>HTTP version of request: '''+ bytes(f'{self.request_version}\n','utf-8') + '''</p>
<p>  </P>
<P>Honestly Im not sure why this wont take these when put in strins. It really bugs me..</P>
</body>
</html>
        
'''
        self.wfile.write(response)


    def do_GET(self):
        try:
            print('in do_GET():')
            print(f"GET {self.path}")
            path = str(self.path).lower()
            print(path)

            # Handling all media
            if '.jpg' in self.path:
                file = str(self.path).strip('/').replace('%20',' ')
                self.serve_file(file)


            # favicon
            elif '.ico' in self.path:
                self.serve_file('favicon.ico')


            # imateapot
            elif self.path == ('/teapot'):
                self.redir418()

            elif path.startswith('/tea'):
                self.redir301('/teapot')


            # 403 forbidden
            elif self.path == ('/forbidden'):
                self.redir403()


            # debugging page
            elif path.startswith('/debugging') or path.startswith('/bug'):
                print('trying the debug page')
                self.redir_debug(path)


            # all style directing
            elif path == '/style.css':
                self.serve_file('style.css')

            elif path.startswith('/style'):
                self.redir301('/style.css')


            # all tips and help directing
            elif self.path == '/tips.html':
                self.serve_file('tips.html')

            elif path.startswith('/tips'):
                self.redir301('/tips.html')

            elif path.startswith('/help'):
                self.redir301('tips.html')


            # all bio and about directing
            elif self.path == '/about.html':
                self.serve_file('about.html')

            elif path.startswith('/bio'):
                self.redir301("/about.html")

            elif path.startswith('/about'):
                self.redir301('/about.html')


            # All index directing
            elif self.path == '/index.html':
                self.serve_file('index.html')

            elif path.startswith('/index') or path.startswith('/'):
                self.redir301('/index.html')

            else:
                # TODO: factor this out into its own function
                self.redir404()
        except:
            self.redir5xx()



if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn1).serve_forever()
    except KeyboardInterrupt:
        quit(1)
