txt = input('camelCase: ')
print('snake_case: ', end='')
c = False
for c in txt:
    if c.islower():
        print(c, end='')
    elif c.isupper():
        print(f'_{c.lower()}', end='')
    c = True
if c != True:
    print(txt)
print()
