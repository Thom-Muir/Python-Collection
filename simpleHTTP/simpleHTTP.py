import http.server
import socketserver
import sys
import os

#Hey, we need a port number here
if len(sys.argv) < 2:
    print(f"{os.path.basename(__file__)} <port> [/path/to/directory]")
    sys.exit(1)
else:
    #Defines port from arg
    try:
        PORT = int(sys.argv[1])
    #Hey, port numbers are typically numbers
    except ValueError:
        print("Port must be a whole number")
        sys.exit(1)
    #If the user has specified a directory, this handles that
    if len(sys.argv) > 2:
        direc = sys.argv[2]
        os.chdir(direc)
        
    #Handler to serve files from directory
    Handler = http.server.SimpleHTTPRequestHandler

    #Server setup
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print(f"Serving at port {PORT} from {os.getcwd()}")
        #Starts the server
        http.serve_forever()
