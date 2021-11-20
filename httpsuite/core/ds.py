import requests
from concurrent.futures import ThreadPoolExecutor
from httpsuite.db.db import directories_db
from httpsuite.core.colors import good, info, bad, blue, bright, reset

def ds(target, threads):
    print('\n' + info + 'Searching Directories...' + '\n')
    if target.endswith('/'):
        print(bad + 'The target ends with "/", Please try again without adding "/" at the end :)')
        quit()
    else:
        pass

    def search(target, dir):
        try:
            build_url = (target + '/' + dir)
            req = requests.get(build_url)
            resp = req.status_code

            if resp == 200:
                print(good + build_url + bright + ' [' + blue + '200' + reset + bright + ']' + reset)
            elif resp == 302:
                print(good + build_url + bright + ' [' + blue + '200' + reset + bright + ']' + reset)
            elif resp == 403:
                print(good + build_url + bright + ' [' + blue + '200' + reset + bright + ']' + reset)
        except KeyboardInterrupt:
            print(bad + 'KeyboardInterrupt!')
            quit()
        except requests.exceptions.ConnectionError:
            print(bad + 'requests.exceptions.ConnectionError:', build_url)

    try:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for dir in directories_db:
                executor.submit(search,target,dir)
    except KeyboardInterrupt:
        print(bad + 'KeyboardInterrupt!')
        quit()