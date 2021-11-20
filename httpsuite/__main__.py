import argparse
from httpsuite.core.header import header
from httpsuite.core.crawl import crawler
from httpsuite.core.subdomains import subdomains
from httpsuite.core.portscan import port_scanner
from httpsuite.core.whois import whois
from httpsuite.core.dns import dnsrec
from httpsuite.core.ds import ds
from httpsuite.core.apf import apf
from httpsuite.core.subscan import subscan
from httpsuite.core.colors import green, reset, bright, bad

print(''' 
    __    __  __                   _ __     
   / /_  / /_/ /_____  _______  __(_) /____ 
  / __ \/ __/ __/ __ \/ ___/ / / / / __/ _ \ 
 / / / / /_/ /_/ /_/ (__  ) /_/ / / /_/  __/
/_/ /_/\__/\__/ .___/____/\__,_/_/\__/\___/ 
             /_/                            
                            @whoamisec
''')
print(bright+green + ':: Author  : '+ reset +'HS Devansh Raghav')
print(bright+green + ':: Version : '+ reset + '1.0')

parser = argparse.ArgumentParser()
parser.add_argument('target', help='Target URL, eg. http://example.com')
parser.add_argument('--headers', help='Header Information, eg. Content-type, Accept, ETag etc.', action='store_true')
parser.add_argument('--crawl', help='Crawl Target', action='store_true')
parser.add_argument('--whois', help='Whois Lookup', action='store_true')
parser.add_argument('--ds', help='Directory Search', action='store_true')
parser.add_argument('--apf', help='Admin Panel Finder', action='store_true')
parser.add_argument('--pscan', help='Multi-Threaded Port Scanner', action='store_true')
parser.add_argument('--dnsrec', help='DNS Enumeration', action='store_true')
parser.add_argument('--subscan', help='Sub-Domain Scanner', action='store_true')
parser.add_argument('--sub-crt', help='Sub-Domain Enumeration Using crt.sh', action='store_true')
ext_help = parser.add_argument_group('Extra Options')
ext_help.add_argument('-c','--concurrency', type=int, help='Specify concurrency [Default : 40]', default=40)
args = parser.parse_args()
target = args.target
headers = args.headers
crawl = args.crawl
sub = args.sub_crt
pscan = args.pscan
Whois = args.whois
dns = args.dnsrec
dbf =  args.ds
_apf = args.apf
_subscan = args.subscan
threads = args.concurrency

def main():
    if headers == True:
        header(target)
    elif crawl == True:
        crawler(target, threads)
    elif sub == True:
        subdomains(target)
    elif pscan == True:  
        port_scanner(target, threads)
    elif Whois == True:
        whois(target)
    elif dns == True:
        dnsrec(target)
    elif dbf == True:
        ds(target, threads)
    elif _apf == True:
        apf(target, threads)
    elif _subscan == True:
        subscan(target, threads)
    else:
        print('\n'+bad + 'No argument supplied!'+'\n')
