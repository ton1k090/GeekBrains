import json
from itertools import zip_longest
import sys


with open("users.csv", "r", encoding="utf-8") as f:
    with open("hobby.csv", "r",encoding="utf-8") as f1:
        users= f.read().replace(',', ' ').splitlines()
        hobby = f1.read().splitlines()
        if len(users) >= len(hobby):
            result_dict = dict(zip_longest(users, hobby))
        else:
            sys.exit(1)
with open('users_hobby.txt', 'w', encoding='utf-8') as f2:
    json.dump(result_dict, f2)
with open('users_hobby.txt', 'r', encoding='utf-8') as f2:
    users_list = json.load(f2)
    print(users_list)
