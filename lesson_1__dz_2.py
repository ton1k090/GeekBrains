cube = [i ** 3 for i in range(1,1001,2)]
sum = 0
summ_cub = 0
for number in cube:
    tmp = number
    while tmp != 0:
        sum += tmp % 10
        tmp = tmp // 10
    if sum % 7 == 0:
        sum = 0
        summ_cub += number
    else:
        sum = 0
print(summ_cub)

