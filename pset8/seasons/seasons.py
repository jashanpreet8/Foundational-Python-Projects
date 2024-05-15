from datetime import date
from sys import exit
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input('Date of Birth: ').split('-')
    except ValueError:
        exit('Invalid input')

    print(minutes(year, month, day))


def minutes(year, month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return 'Invalid Date'
    tdy = date.today()
    diff = tdy - dt
    minutes = int(diff.total_seconds() / 60)

    return (p.number_to_words(minutes, andword='') + ' minutes')

if __name__ == "__main__":
    main()