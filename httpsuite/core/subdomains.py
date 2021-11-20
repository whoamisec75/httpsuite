import re
import requests, json, sys
from httpsuite.core.colors import info, bad, good, red, green, bright, reset

def subdomains(target):
    try:
        print('\n'+ info + 'Finding subdomains using crt.sh...'+ '\n')
        if re.search('https://', target):
            target = target.replace('https://', '')
        elif re.search('http://', target):
            target = target.replace('http://', '')
    
        req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))
        json_data = json.loads(req.text)
        for (key,value) in enumerate(json_data):
            print(value['name_value'])
    except KeyboardInterrupt as k:
        print(bad + 'KeyboardInterrupt!')
        quit()
    


