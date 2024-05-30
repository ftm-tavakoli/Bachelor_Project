import requests
from bs4 import BeautifulSoup
import re
import os

sites = []
f = open("netmeds.txt", "r")
sites.append(f.readlines())
f.close()
sites = sites[0]
sites_2 = []
for x in sites:
    # sites_2.append(x.replace('\n', ''))
    x = 'https://' + x
    x = x.replace('\n', '')
    r = requests.get(f'{x}').content
    soup = BeautifulSoup(r, 'lxml')
    reg = re.findall("""https://www\.netmeds\.com/images/product-v1/600x600/.*?\.jpg""", str(soup))
    try:
        if 'tablets' in reg[0]:
            continue
        else:
            os.system(f'wget {reg[0]}')

    except:
        print('EMPTY')
    # print(reg[0])
    # try:
    #     os.system(f'wget {reg[0]}')
    # except:
    #     print("EMPTY")