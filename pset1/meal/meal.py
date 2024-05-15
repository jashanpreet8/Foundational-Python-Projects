def main():
    t = input('Time: ')
    t = convert(t)
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')

def convert(t):
    h, m = t.split(':')
    h = int(h)
    m = int(m)
    m = float(m/60)
    time = h + m
    return time

if __name__ == "__main__":
    main()