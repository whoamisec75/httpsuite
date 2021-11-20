import requests
from httpsuite.core.colors import reset, red, good, bad, info, bright, yellow, cyan
requests.packages.urllib3.disable_warnings()

def header(target):
    print('\n'+ info +'Headers =>' + '\n')
    try:
        req = requests.get(target, verify=False, timeout=10)
        for key, value in req.headers.items():
            print(good + bright + cyan + '{}: '.format(key) + reset +value)
    except KeyboardInterrupt as k:
        print(bad + 'KeyboardInterrupt!')
        quit()

