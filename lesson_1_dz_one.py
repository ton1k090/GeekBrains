duration = int(input("Введите время в секундах: "))
sec = "секунд(ы)"
min = "минут"
hour = "час(а)"
day = "день(дней)"
if duration <= 60:
    second = f"{duration} {sec}"
    print(second)
elif duration <= 3600:
    a = str(duration // 60)
    b = str((duration % 3600) % 60)
    minute = f"{a} {min} {b} {sec}"
    print(minute)
elif duration <= 86400:
    a = str(duration // 3600)
    b = str(duration // 60)
    c = str((duration % 3600) % 60)
    hours = f"{a} {hour} {b} {min} {c} {sec}"
    print(hours)
elif duration >= 86400:
    a = str(duration // 86400)
    b = str(duration // 3600)
    c = str(duration // 60)
    d = str((duration % 3600) % 60)
    day = f"{a} {day} {b} {hour} {c} {min} {d} {sec}"
    print(day)



