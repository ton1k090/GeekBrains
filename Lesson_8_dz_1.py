import re

def email_parse(email_address):

    pattern = re.compile(r"(?P<username>\w+)@(?P<domain>\w+\.\w{2,3})")
    result = pattern.match(email_address)
    result_iter = pattern.finditer(email_address)
    for el in result_iter:
        return el.groupdict()
    if result == None:
        raise ValueError(f'Не верный адресс электронной почты: {email_address}')

print(email_parse("someone@geekbrains.ru"))
print(email_parse("someone@geekbrains.r"))
print(email_parse("someone@geekbrainsru"))