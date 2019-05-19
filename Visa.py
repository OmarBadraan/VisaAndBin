import requests
import random
from bs4 import BeautifulSoup as bs
from pyfiglet import Figlet
banner = Figlet(font='small')


print(banner.renderText('OmarBadraan'))
print('++++' * 18)

file = open('omarbadraan_visa.txt', 'w')

def card(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

visabin = input('Please enter a valid Bin: ')

chrs = '0123456789'

while True:
    chrz = random.sample(chrs, len(chrs))
    visa = visabin + ''.join(chrz)
    if card(visa) == True:
        file.write('[+] Found Visa : ' + visa + '\n')
        pass
