from colorama import Fore, init, Style
import threading
import requests
import ctypes
import os

os.system('cls')
init(convert=True, autoreset=True)
lock = threading.Lock()
SentCounter = 0
ErrorCounter = 0


ctypes.windll.kernel32.SetConsoleTitleW('YoloRape | Made By Icey')
print(Fore.YELLOW + Style.BRIGHT + ' /$$     /$$        /$$           /$$$$$$$                               ')
print(Fore.YELLOW + Style.BRIGHT + '|  $$   /$$/       | $$          | $$__  $$                              ')
print(Fore.YELLOW + Style.BRIGHT + ' \  $$ /$$//$$$$$$ | $$  /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$ ')
print(Fore.YELLOW + Style.BRIGHT + '  \  $$$$//$$__  $$| $$ /$$__  $$| $$$$$$$/ |____  $$ /$$__  $$ /$$__  $$')
print(Fore.YELLOW + Style.BRIGHT + '   \  $$/| $$  \ $$| $$| $$  \ $$| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$$$')
print(Fore.YELLOW + Style.BRIGHT + '    | $$ | $$  | $$| $$| $$  | $$| $$  \ $$ /$$__  $$| $$  | $$| $$_____/')
print(Fore.YELLOW + Style.BRIGHT + '    | $$ |  $$$$$$/| $$|  $$$$$$/| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$')
print(Fore.YELLOW + Style.BRIGHT + '    |__/  \______/ |__/ \______/ |__/  |__/ \_______/| $$____/  \_______/')
print(Fore.YELLOW + Style.BRIGHT + '                                                     | $$                ')
print(Fore.YELLOW + Style.BRIGHT + '                                                     | $$                ')
print(Fore.YELLOW + Style.BRIGHT + '                                                     |__/                ')
print(Fore.WHITE + Style.BRIGHT + 'URL:')
URL = str(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
try:
    URLCode = URL.split('https://onyolo.com/m/')[1].split('?')[0]
except IndexError:
    print(' ')
    print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Invalid URL')
    input()
    quit()
print(Fore.WHITE + Style.BRIGHT + '\nMessage:')
message = str(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(Fore.WHITE + Style.BRIGHT + '\nThreads:')
threads = int(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(Fore.WHITE + Style.BRIGHT + '\nAmount:')
amount = int(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(' ')

def Spammer():
    global SentCounter
    global ErrorCounter
    try:
        session = requests.Session()
        headers = {
            'path': '/' + str(URLCode) + '/message',
            'content-type': 'application/json;charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        data = '{"text":"' + str(message) + '","cookie":"5w5j5djvvk3snnf5llrrfo","wording":"Send honest messages"}'
        POST = session.post('https://onyolo.com/' + str(URLCode) + '/message', headers=headers, data=data)
        if 'ok' in POST.text:
            SentCounter += 1
            lock.acquire()
            print(Fore.LIGHTMAGENTA_EX + '[ONED] ' + Fore.WHITE + Style.BRIGHT + 'Sent message | #' + str(SentCounter))
            lock.release()
            ctypes.windll.kernel32.SetConsoleTitleW('Yolo Rape | Sent: ' + str(SentCounter) + ' | Errors: ' + str(ErrorCounter) + ' | Made By Icey')
        elif 'Forbidden' in POST.text:
            ErrorCounter += 1
            lock.acquire()
            print(Fore.MAGENTA + '[NICE MISS] ' + Fore.WHITE + Style.BRIGHT + 'Ratelimited')
            lock.release()
            ctypes.windll.kernel32.SetConsoleTitleW('Yolo Rape | Sent: ' + str(SentCounter) + ' | Errors: ' + str(ErrorCounter) + ' | Made By Icey')
        else:
            print(POST.text)
    except Exception as e:
        print(e)

for i in range(amount):
    threading.Thread(target=Spammer, args=()).start()
input()