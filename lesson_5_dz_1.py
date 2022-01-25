def odd_nums(numb):
    for i in range(1, numb + 1, 2):
        yield i

odd_to_5 = odd_nums(5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))