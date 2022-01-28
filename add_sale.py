import sys

if sys.argv != 0:
    with open("bakery.csv", "a", encoding="utf-8") as price_f:
        input_f = f"{sys.argv[1]}\n"
        price_f.write(input_f)

