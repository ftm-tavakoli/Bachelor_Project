import requests
from bs4 import BeautifulSoup
import re
import os

count = 0
sites = []
f = open("links.txt", "r")
sites.append(f.readlines())
f.close()
sites = sites[0]
sites_2 = []
for x in sites:
    sites_2.append(x.replace('\n', ''))


for x in range(len(sites_2)):
    r = requests.get(f'{sites_2[x]}').content
    soup = BeautifulSoup(r, 'lxml')
    reg = str(soup)
    try:
        result = re.findall('<img[^>]*src="[^"]*', reg)
        down = 'https://www.ukmeds.co.uk'+result[17][81:]
        print(down)
        os.system(f'wget {down}')
    except:
        print("=========ERROR========")
        count += 1

