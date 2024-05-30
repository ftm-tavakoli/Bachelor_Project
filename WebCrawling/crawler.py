import requests
import re
from urllib.parse import urlparse

class PyCrawler(object):


    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()

    def get_html(self, url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    def get_links(self, url):
        html = self.get_html(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)
        for i, link in enumerate(links):
            if not urlparse(link).netloc:
                link_with_base = base + link
                links[i] = link_with_base

        return set(filter(lambda x: 'mailto' not in x, links))

    def extract_info(self, url):
        html = self.get_html(url)
        return None

    def crawl(self, url):
        for link in self.get_links(url):
            if link in self.visited:
                continue
            print(link)
            # with open('links.txt', 'a+') as link:
            #     link.write(str(link))

            f = open("links.txt", "a")
            f.writelines(str(link)+'\n')
            f.close()

            self.visited.add(link)
            info = self.extract_info(link)
            self.crawl(link)

    def start(self):
        self.crawl(self.starting_url)

if __name__ == "__main__":
    crawler = PyCrawler("https://www.chemistwarehouse.com.au/shop-online/542/fragrances")
    crawler.start()