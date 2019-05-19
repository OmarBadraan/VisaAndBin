import requests
import random
from bs4 import BeautifulSoup as bs
from pyfiglet import Figlet
banner = Figlet(font='small')


print(banner.renderText('OmarBadraan\n'))
chrs = '9876543210'
file = open('omarbadraan_bin.txt', 'w')

def Check():
    while True:
        part = random.sample(chrs, 6)
        web = requests.get('https://bincheck.org/' + ''.join(part))
        soup = bs(web.text, 'html.parser')
        if soup.findAll("p", class_="notice monts") == []:
            print("[+] Found Validate Bin:", ''.join(part))
            file.write(''.join(part) + '\n')

Check()
