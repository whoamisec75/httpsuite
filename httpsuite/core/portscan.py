import socket
import threading
import re
import concurrent.futures
from colorama import Fore, Style
from httpsuite.core.colors import good, bright, info, reset,bad

def port_scanner(target, threads):
    try:
        print('\n'+ info + 'Starting port scanner...')
        if re.search('https://', target):
            target = target.replace('https://', '')
        elif re.search('http://', target):
            target = target.replace('http://', '')
        print_lock = threading.Lock()
        port_range = input('\n' + bright +"Scan up to port (example would be 1000): " + reset)
        print('')
        def scan(target, port):
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.settimeout(1)

            try: 
                scanner.connect((target, port))
                service = socket.getservbyport(port, 'tcp')
                scanner.close()

                with print_lock:
                    print(good + 'OPEN:', port, service)
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for port in range(int(port_range)):
                executor.submit(scan, target, port + 1)
    except KeyboardInterrupt as k:
        print(bad + 'KeyboardInterrupt!')
        quit()