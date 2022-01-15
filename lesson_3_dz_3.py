def thesaurus(*args):
    items = {}
    for name in args:
        key = name[0]
        val = name
        if key not in items:
            items[key] = []
        items[key].append(val)
    print(items)


thesaurus("Иван", "Мария", "Петр", "Илья", "Олег", "Филипп", "Милана")

