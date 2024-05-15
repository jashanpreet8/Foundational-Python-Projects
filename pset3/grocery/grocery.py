items = {}
while True:
    try:
        item = input('').upper()
        if item not in items:
            items[item] = 1
        elif item in items:
            items[item] += 1
    except EOFError:
        print()
        break

myKeys = list(items.keys())
myKeys.sort()
items = {i: items[i] for i in myKeys}

for item in items:
    print(items[item], end='')
    print(' ' + item)