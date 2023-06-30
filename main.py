import time
import codecs
from colorama import init, Fore, Back, Style
from os import system


clear = lambda: system('cls')
clear()

system("title " + '[TELEGRAM MSG SENDER]')
print()
print()


init(autoreset=True)

print(Style.NORMAL + Back.BLACK + Fore.RED)

time.sleep(2)

print()

txtLoading = 'LOADING...'
txtAuthor = 'SCRIPT BY >>> @TudoEstranho'
for i in range(10):
    print(txtLoading[i], sep=' ', end=' ', flush=True); time.sleep(0.1)
 
for i in range(23):
    print(txtAuthor[i], sep='', end='', flush=True); time.sleep(0.1)

print()
print()

f = open('UserList.txt')
lines = f.read().splitlines()
f.close()

delay = input("[+] Please set delay bettwen per message(sec): ")
print("[+] Good. delay has been set to: " + delay + " sec")
print()

from telethon import TelegramClient , events , sync

#######CLIENT INFORMATION#######

api_id = 'PUT YOUR API ID OUTSIDE OF SINGLE QUOTES'
api_hash = "PUT YOUR API HASH INSIDE THE DOUBLE QUOTES"

#######START WITH CREDENTIALS#######

client = TelegramClient("SESSION" , api_id , api_hash)
client.start()

#######SEND MSG TO USERS#######

f1 = codecs.open('Msg.txt', "r", "utf-8")
msg = f1.read()
f1.close()

message = msg

for uname in lines:
    client.send_message(uname , message)
    print(Style.NORMAL + Back.BLACK + Fore.GREEN + "sending message to {}".format(uname))
    time.sleep(int(delay))
    
print('Done!')

client.disconnect()