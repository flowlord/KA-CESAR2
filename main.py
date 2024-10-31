import json
from key_generator import keys
from random import choice

with open('setting.json', 'r') as openfile:
        load_file = json.load(openfile)
all_charac = load_file["charac_lst"]

def ka_cipher(plain_text, key):

    key = dict(zip(all_charac, key))
    new_text = ""

    for c in plain_text:
        new_text = new_text + key[c]

    return new_text


def ka_decipher(code, key):

    key = dict(zip(key, all_charac))
    new_text = ""

    for c in code:
        new_text = new_text + key[c]

    return new_text


def ka_cipher_rand(plain_text):
    return ka_cipher(plain_text, choice(keys))

def ka_decipher_rand(plain_text):
    ke = True
    new_text = ""

    while ke:
        key = choice(keys)
        try:
            new_text = ka_decipher(plain_text, key)
            ke = False
        except KeyError:
            pass
    
    return new_text


msg = ka_cipher_rand("Bonjour Tous le Monde !$")
print(msg)

print(ka_decipher_rand(msg))


