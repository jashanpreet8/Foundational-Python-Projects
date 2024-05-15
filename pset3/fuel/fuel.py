while True:
    try:
        fra = input('Fraction: ')
        n, d = fra.split('/')
        if n.isdigit() and d.isdigit() and int(n) <= int(d):
            break
    except ValueError or ZeroDivisionError:
        pass
out = round(int(n)*100/int(d))
if out <= 1:
    print('E')
elif out >= 99:
    print('F')
else:
    print(f'{out}%')