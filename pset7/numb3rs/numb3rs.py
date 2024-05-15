import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip.strip()
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        list = ip.split('.')
        for i in list:
            if i not in range(256):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()