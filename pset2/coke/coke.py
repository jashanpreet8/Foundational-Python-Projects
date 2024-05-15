amt = 50
while True:
    print(f'Amount Due: {amt}')
    ins = int(input('Insert Coin: '))
    if ins == 25 or ins == 10 or ins == 5:
        amt -= ins
    if amt <= 0:
        break
print(f'Change Owed: {-1*amt}')