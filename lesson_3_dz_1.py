def num_translate(eng):
    translation = { "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    return translation.get(eng)

print(num_translate("two"))

