from random import shuffle
from setting_generator import gen_setting_file, NBR_KEYS
import json

try:
    with open('setting.json', 'r') as openfile:
        load_file = json.load(openfile)
except FileNotFoundError:
    gen_setting_file(NBR_KEYS)
    with open('setting.json', 'r') as openfile:
        load_file = json.load(openfile)

def gen_random_setting():
    all_charac = list(load_file["charac_lst"])
    shuffle(all_charac)
    return ''.join(all_charac)


def gen_keys_file():
    nbr_keys = load_file["nbr_keys"]
    outfile =  open("keys.kac2", "w", encoding="utf-8")

    for _ in range(nbr_keys):
        outfile.write(gen_random_setting() + "\n")

    outfile.close()


try:
    keys =  [key.replace("\n", "") for key in open("keys.kac2", "r").readlines()]
except FileNotFoundError:
    gen_keys_file()


