import requests
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style
import os
from httpsuite.core.colors import good, info, bad

def crawler(target, threads):
    class MultiThreadScraper:

        def __init__(self, base_url):

            self.base_url = base_url
            self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)
            self.pool = ThreadPoolExecutor(max_workers=threads)
            self.scraped_pages = set([])
            self.to_crawl = Queue()
            self.to_crawl.put(self.base_url)

        def parse_links(self, html):
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                url = link['href']
                if url.startswith('/') or url.startswith(self.root_url):
                    url = urljoin(self.root_url, url)
                    if url not in self.scraped_pages:
                        self.to_crawl.put(url)

        def scrape_info(self, html):
            return

        def post_scrape_callback(self, res):
            result = res.result()
            if result and result.status_code == 200:
                self.parse_links(result.text)
                self.scrape_info(result.text)

        def scrape_page(self, url):
            try:
                res = requests.get(url, timeout=(3, 30))
                return res
            except requests.RequestException:
                return

        def run_scraper(self):
            while True:
                try:
                    target_url = self.to_crawl.get(timeout=60)
                    if target_url not in self.scraped_pages:
                        print(good+ f"{target_url}")
                        self.scraped_pages.add(target_url)
                        job = self.pool.submit(self.scrape_page, target_url)
                        job.add_done_callback(self.post_scrape_callback)
                except Empty:
                    return
                except KeyboardInterrupt as k:
                    print(bad + 'KeyboardInterrupt!')
                    quit()
                except:
                    continue
    print('\n'+ info +'Starting crawler...' + '\n')             
    cl = target           
    s = MultiThreadScraper(cl)
    s.run_scraper()