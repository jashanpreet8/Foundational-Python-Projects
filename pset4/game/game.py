from random import randint
while True:
    num = input('Level: ')
    if int(num) > 0:
        break
gu = randint(1, num)
while True:
    try:
        guess = input('Guess: ')
        if guess < gu:
            print('Too small!')
        elif guess > gu:
            print('Too large!')
        else:
            print('Just right!')
            break
    except:
        pass