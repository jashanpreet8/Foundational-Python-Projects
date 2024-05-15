def main():
    while True:
        fraction = input('Fraction: ')
        percentage = convert(fraction)
        if convert(fraction) == percentage:
            break

    print(gauge(percentage))


def convert(fraction):
    try:
        n, d = fraction.split('/')
        if n.isdigit() and d.isdigit() and int(n) <= int(d):
            percentage = round(int(n)*100/int(d))
            return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()