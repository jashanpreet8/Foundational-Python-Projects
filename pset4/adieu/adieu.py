import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        print()
        break

"""
#my approach
length = len(names)
print('Adieu, adieu, to ', end='')
for name in names:
    if length == 1:
        print(name)
    elif names.index(name) == length-1:
        print(f'and {name}')
    else:
        print(f'{name}, ',end='')
"""

out = p.join(names)
print('Adieu, adieu, to ' + out)