from sys import exit, argv
import csv
from tabulate import tabulate

if len(argv) != 2:
    print('Input valid command-line arguments')
    exit(1)

infile = argv[1]
index = infile.index('.')

if infile[index:] != '.csv':
    print("Input '.csv' file!")
    exit(1)

try:
    file = open(infile, 'r')
except FileNotFoundError:
    print('Enter valid file!')
    exit(1)
file.close()

menu = []
with open(infile) as file:
    reader = csv.reader(file)
    for row in reader:
        menu.append(row)


print(tabulate(menu[1:], headers=menu[0], tablefmt='grid'))