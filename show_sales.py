import sys


with open("bakery.csv", "r", encoding="utf-8") as price_f:
    if len(sys.argv) == 1:
        print(price_f.read())
    elif len(sys.argv) == 2:
        content = price_f.read().splitlines()
        content.pop(0)
        print('\n'.join(content[int(sys.argv[1]) - 2:]))
    elif len(sys.argv) == 3:
        content = price_f.read().splitlines()
        content.pop(0)
        print('\n'.join(content[int(sys.argv[1]) - 2:int(sys.argv[2])]))
    else:
        sys.exit(1)