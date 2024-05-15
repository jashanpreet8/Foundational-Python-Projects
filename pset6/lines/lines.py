from sys import argv, exit

if len(argv) != 2:
    print('Input 2 command-line arguments!')
    exit(1)

infile = argv[1]
index = infile.index('.')

if infile[index:] != '.py':
    print("Input '.py' file!")
    exit(1)

try:
    file = open(infile, 'r')
    lines = file.readlines()
except FileNotFoundError:
    print('Enter valid file!')
    exit(1)

count = 0
for line in lines:
    if line.isspace():
        pass
    elif line.lstrip().startswith('#'):
        pass
    else:
        count += 1


print(count)
