from sys import exit, argv
from PIL import Image, ImageOps

def main():
    infile = argv[1]
    outfile = argv[2]
    validity(infile, outfile)

    try:
        image = Image.open(infile)
    except FileNotFoundError:
        exit('Enter valid file!')

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirt, shirt)
    muppet.save(outfile)


def validity(infile, outfile):
    if len(argv) != 3:
        exit('Input valid command-line arguments')

    index1 = infile.index('.')
    index2 = outfile.index('.')

    if infile[index1:].lower() not in ['.jpg', '.jpeg', '.png']:
        exit("Input file invalid!")

    if outfile[index2:].lower() not in ['.jpg', '.jpeg', '.png']:
        exit("Output file invalid!")

    if infile[index1:] != outfile[index2:]:
        exit('Enter same extension files')


if __name__ == "__main__":
    main()