def main():
    word = input('Input: ')
    print(f'Output: {shorten(word)}')

def shorten(word):
    word = word.replace('a', '')
    word = word.replace('e', '')
    word = word.replace('i', '')
    word = word.replace('o', '')
    word = word.replace('u', '')
    return word

if __name__ == "__main__":
    main()