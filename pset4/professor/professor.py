import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        i += 1
        wrong = 0
        while True:
            print(f'{x} + {y} = ', end='')
            try:
                ans = int(input(''))
                if ans == z:
                    score += 1
                    break
                else:
                    wrong += 1
                    print('EEE')
            except ValueError:
                wrong += 1
                print('EEE')
            if wrong == 3:
                print(f'{x} + {y} = {z}')
                break
    print('Score: ', score)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        rand_int = random.randint(0, 9)
    elif level == 2:
        rand_int = random.randint(10, 99)
    elif level == 3:
        rand_int = random.randint(100, 999)
    return rand_int

if __name__ == "__main__":
    main()