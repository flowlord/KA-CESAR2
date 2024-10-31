from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import json

NBR_KEYS = 3

def gen_setting_file(nbr_keys):
    
    json_object = json.dumps({"charac_lst": ascii_lowercase + ascii_uppercase + digits + punctuation+" ", "nbr_keys":nbr_keys}, indent=4)
    
    with open("setting.json", "w") as outfile:
        outfile.write(json_object)



