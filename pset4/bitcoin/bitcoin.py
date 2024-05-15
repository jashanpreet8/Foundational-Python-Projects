from sys import exit, argv
import requests
import json

if len(argv) != 2:
    print('Missing command-line argument')
    exit(1)
try:
    n = float(argv[1])
except ValueError:
    print('Command-line argument is not a number ')
    exit(1)

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print('error in request')

o = response.json()
rate = o['bpi']['USD']['rate_float']
amount = rate*n
print(f'${amount:,.4f}')