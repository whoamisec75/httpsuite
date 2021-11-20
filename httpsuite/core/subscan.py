import re
import requests
from concurrent.futures import ThreadPoolExecutor
from httpsuite.db.db import subdomains_db
from httpsuite.core.colors import good, info, bad, blue, bright, reset

def subscan(target, threads):
    print('\n' + info + 'Scanning Subdomains...' + '\n')
    if re.search('https://', target):
        target = target.replace('https://', '')
    elif re.search('http://', target):
        target = target.replace('http://', '')
    else:
        target = target
    
    def search(target, subdomain):
        try:
            build_url = (f'http://{subdomain}.{target}')
            req = requests.get(build_url)
            resp = req.status_code

            if resp == 200:
                print(good + build_url)
        except KeyboardInterrupt:
            print(bad + 'KeyboardInterrupt!')
            quit()
        except requests.exceptions.ConnectionError:
            pass

    try:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for dir in subdomains_db:
                executor.submit(search,target,dir)
    except KeyboardInterrupt:
        print(bad + 'KeyboardInterrupt!')
        quit()  