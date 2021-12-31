


for n in range(1,101):
    if n % 10 == 1 and n != 11:
        print(f"{n} процент")
    elif 5 <= n <= 20:
        print(f"{n} процентов")
    elif 2 <= n <= 4 or n % 10 == 2:
        print(f"{n} процента")
    elif n % 10 == 3:
        print(f"{n} процента")
    elif n % 10 == 4:
        print(f"{n} процента")
    else:
        print(f"{n} процентов")
