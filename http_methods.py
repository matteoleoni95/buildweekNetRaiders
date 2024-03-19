import http.client

host = input("Inserire Host/IP del sistema target: ")
port = input("Inserire la porta del sistema target (default: 80): ")
path = input("Inserire path da controllare (default /): ").strip()

if (port == ""):
	port = 80
else:
	port = int(port)

if (path == ""):
	path = "/"

try:
	connection = http.client.HTTPConnection(host, port)
	connection.request("OPTIONS", path)
	response = connection.getresponse()
	print("Lo status e' : ", response.status)
	if response.status in (301,302,303,307,308):
		redirect = response.getheader("Location")
		print(f"Reindirizzamento ({response.status}) a: {redirect}")
	else:
		methods_enabled = response.getheader("allow")
		print("I metodi abilitati sono: ", methods_enabled)
	connection.close()
except ConnectionRefusedError:
	print("Connessione Fallita")

