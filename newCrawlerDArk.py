import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class DarkWebCrawler:
    def __init__(self, url, max_depth=2):
        self.url = url
        self.max_depth = max_depth
        self.visited = set()

    def is_valid(self, url):
        return url.endswith('.onion') and url not in self.visited

    def crawl(self):
        self.visited.add(self.url)
        try:
            response = requests.get(self.url, timeout=40)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"[+] Crawling {self.url}")
            self.extract_emails(soup)
            self.extract_files(soup, [r'\.(txt|pdf)$', r'password', r'secret', r'username'])
            for link in soup.find_all('a'):
                href = link.get('href')
                if self.is_valid(href):
                    crawler = DarkWebCrawler(urljoin(self.url, href), self.max_depth)
                    if crawler.max_depth > len(self.visited):
                        crawler.crawl()
        except Exception as e:
            print(f"[-] Error: {e}")

    def extract_emails(self, soup):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_regex, str(soup))
        for email in emails:
            print(f"[+] Email: {email}")

    def extract_files(self, soup, patterns):
        for pattern in patterns:
            if isinstance(pattern, str):
                file_regex = re.compile(pattern)
                for match in re.findall(file_regex, str(soup)):
                    print(f"[+] Found file/keyword: {match}")
            elif isinstance(pattern, list):
                tag, attr, value = pattern
                for elem in soup.find_all(tag, {attr: value}):
                    print(f"[+] Found file/keyword: {elem.text}")

if __name__ == "__main__":
    url = input("Enter the onion URL to crawl: ")
    crawler = DarkWebCrawler(url)
    crawler.crawl()
