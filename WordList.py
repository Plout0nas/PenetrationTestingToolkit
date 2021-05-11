import itertools
import os


def generateWordlist(minSize, maxSize, types, name):
    pass

    try:
        os.system("")
    except:
        print("")
    # minSize = int(input('Minimum size of the words : '))
    # maxSize = int(input('Maximum size of the words : '))
    print("\n[1] Only alphabets\n[2] Only Numbers\n[3] Alphanumeric\n")
    # types = int(input('Your choice : '))

    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    alphaNumeric = alpha + num


    # name = input('Set the name(or path) of the wordlist to be created : ')

    list = [alpha, num, alphaNumeric]

    file = open(name, "w")
    count = 0

    for i in range(minSize, maxSize + 1):
        for xs in itertools.product(list[types - 1], repeat=i):
            file.write(''.join(xs) + '\n')
            print(''.join(xs))
            count += 1

    file.close()

# print("\n\033[1;32;40m[+] Wordlist generated : " + name + " - " + str(count) + " lines")
