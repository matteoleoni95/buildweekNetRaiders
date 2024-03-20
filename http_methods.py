import requests

#inserimento host, porta e path da cercare
host = input("Inserire Host/IP del sistema target: ").strip()
port = input("Inserire la porta del sistema target (default: 80): ").strip()
path = input("Inserire path da controllare (default /): ").strip()

#Se non viene inserita una porta, di default è 80
if (port == ""):
    port = 80
else:
    port = int(port)

#Se il path non viene inserito, di default è "/"
if (path == ""):
    path = "/"

try:

    #Crea la stringa con l'indirizzo da fare la request, se non viene specificato in input l'http viene aggiunto
    if(host.startswith('http')):
        address = f"{host}:{port}{path}"
    else:
        address = f"http://{host}:{port}{path}"
    print (address)
    
    #Prova ad eseguire una richiesta in 'OPTIONS'
    response = requests.options(address)
    print("Lo status e' : ", response.status_code)
    
    #Se lo stato è di redirect, stampa la pagina a cui ridirige
    if response.status_code in (301,302,303,307,308):
        redirect = response.headers.get("Location")
        print(f"Reindirizzamento ({response.status_code}) a: {redirect}")
        
    #Altrimenti procede a stampare i metodi abilitati
    else:
        methods_enabled = response.headers.get("allow")
        print("I metodi abilitati sono: ", methods_enabled)
        
        #se ci sono eccezioni, le stampa
except Exception as e:
    print(e)
