import sys
from modules import keyGen, server, client

mode = sys.argv[1] # Get server mode from cmdline argument.

if mode == "server": # Start server
	server.startServer()
elif mode == "client": # Start client
	client.startClient()
else:
	print("Error. Please see documentation for usage instructions.")
	sys.exit(0)
