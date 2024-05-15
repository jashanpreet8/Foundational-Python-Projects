import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s.strip()
    times = re.search("^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    if times:
        h1 = int(times.group(1))
        if times.group(2):
            m1 = int(times.group(2))
            if m1 > 59:
                raise ValueError('Invalid format')
        else:
            m1 = 0
        z1 = times.group(3)
        h2 = int(times.group(4))
        if times.group(5):
            m2 = int(times.group(5))
            if m2 > 59:
                raise ValueError('Invalid format')
        else:
            m2 = 0
        z2 = times.group(6)

        if h1 > 12 or h2 > 12:
            raise ValueError('Invalid format')

        if z1 == 'AM':
            pass
        if z2 == 'AM':
            pass
        if z1 == 'PM':
            h1 += 12
        if z2 == 'PM':
            h2 += 12

        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    else:
        raise ValueError('Invalid Format')


if __name__ == "__main__":
    main()