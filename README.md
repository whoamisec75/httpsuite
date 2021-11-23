<p align="center"><img src="https://github.com/whoamisec75/httpsuite/blob/main/static/IMG_20211122_204717.jpg"/></p>
<i><b><p align="center">A toolkit for web reconnaissance, it's fast and easy to use.</p></b></i>  

## File Structure
* httpsuite/
  * main.py
  * init.py
  * db/
    * db.py
      * init.py
      * subdomains_db
      * directories_db
      * adminfinder_db
  * core/
    * init.py
    * apf.py
    * colors.py
    * crawl.py
    * dns.py
    * ds.py
    * header.py
    * portscan.py
    * subdomains.py
    * subscan.py
    * whois.py
* setup.py
* README.md
* .gitignore
* LICENCE

## Installation 

```
$ git clone https://github.com/whoamisec75/httpsuite
$ cd httpsuite
$ sudo python3 setup.py install
$ httpsuite -h
```

## Usage 
<img src="https://github.com/whoamisec75/httpsuite/blob/main/static/Screenshot%20from%202021-11-20%2022-37-22.png" length="600px" width="600px"/>

## Whois lookup
```
$ httpsuite http://example.com --whois
```
## Header information
```
$ httpsuite http://example.com --headers
```
## Crawling
```
$ httpsuite http://example.com --crawl
```
## Directory Search
```
$ httpsuite http://example.com --ds
```
## Admin Panel Finder
```
$ httpsuite http://example.com --ds
```
## Port Scanning
```
$ httpsuite http://example.com --pscan
```
## DNS Enumeration
```
$ httpsuite http://example.com --dnsrec
```
## Subdomain Scanning
```
$ httpsuite http://example.com --subscan
```
## Subdomain Scanning using crt.sh
```
$ httpsuite http://example.com --sub-crt
```
