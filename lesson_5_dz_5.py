

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_src = set()
repeated_src = set()
for unique in src:
    if unique in repeated_src:
        continue
    if unique in unique_src:
        unique_src.remove(unique)
        repeated_src.add(unique)
        continue
    unique_src.add(unique)

print(unique_src)

