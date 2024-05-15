from sys import exit, argv
import csv

if len(argv) != 3:
    print('Input valid command-line arguments')
    exit(1)

infile = argv[1]
outfile = argv[2]
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

with open(infile) as before:
    reader = csv.DictReader(before)
    with open(outfile, 'w') as after:
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])
        writer.writerow({'first':'first', 'last':'last', 'house':'house'})
        for row in reader:
            last, first = row['name'].split(',')
            writer.writerow({'first':first.lstrip(), 'last':last, 'house':row['house']})
