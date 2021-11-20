import re
import socket
import ipwhois
from httpsuite.core.colors import good, bad, info, bright, reset, cyan

def whois(target):
    print('\n'+info + 'Whois Lookup :'+'\n')
    if re.search('https://', target):
        target = target.replace('https://', '')
    elif re.search('http://', target):
        target = target.replace('http://', '')
    else:
        target = target

    ip = socket.gethostbyname(target)

    try:
        lookup = ipwhois.IPWhois(ip)
        result = lookup.lookup_whois()

        for key, value in result.items():
            if value != None:
                if isinstance(value, list):
                    for item in value:
                        for key, value in item.items():
                            if value != None:
                                print (good + bright + cyan +'{}:'.format(str(key)) + reset, str(value).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))
                            else:
                                pass
                else:
                    print (good + bright + cyan +'{}:'.format(str(key)) + reset, str(value).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))

            else:
                pass
    except KeyboardInterrupt as k:
        print(bad + 'KeyboardInterrupt!')
        quit()
    except:
        pass

	


    