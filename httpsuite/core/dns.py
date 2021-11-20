import os
import re
import dnslib
from httpsuite.core.colors import bad, good, info

def dnsrec(target):
    if re.search('https://', target):
        target = target.replace('https://', '')
    elif re.search('http://', target):
        target = target.replace('http://', '')
    else:
        target = target
    try:
	    print('\n'+ info + 'Starting DNS Enumeration...' + '\n')
	    types = ['A', 'AAAA', 'ANY', 'CAA', 'CNAME', 'MX', 'NS', 'TXT']
	    full_ans = []
	    for Type in types:
		    q = dnslib.DNSRecord.question(target, Type)
		    pkt = q.send('8.8.8.8', 53, tcp='UDP')
		    ans = dnslib.DNSRecord.parse(pkt)
		    ans = str(ans)
		    ans = ans.split('\n')
		    full_ans.extend(ans)
	    full_ans = set(full_ans)
	    dns_found = []

	    for entry in full_ans:
		    if entry.startswith(';') == False:
			    dns_found.append(entry)
		    else:
			    pass
	
	    if len(dns_found) != 0:
		    for entry in dns_found:
			    print(good + ' {}'.format(entry))
	    else:
		    print(bad + ' DNS Records Not Found!')
	
	    dmarc_target = '_dmarc.' + target
	    q = dnslib.DNSRecord.question(dmarc_target, 'TXT')
	    pkt = q.send('8.8.8.8', 53, tcp='UDP')
	    dmarc_ans = dnslib.DNSRecord.parse(pkt)
	    dmarc_ans = str(dmarc_ans)
	    dmarc_ans = dmarc_ans.split('\n')
	    dmarc_found = []

	    for entry in dmarc_ans:
		    if entry.startswith('_dmarc') == True:
			    dmarc_found.append(entry)
		    else:
			    pass
	    if len(dmarc_found) != 0:
		    for entry in dmarc_found:
			    print(good + ' {}'.format(entry))
	    else:
		    print('\n' + good +' DMARC Record Not Found!')

    except KeyboardInterrupt:
        print(bad + 'KeyboardInterrupt!')
		