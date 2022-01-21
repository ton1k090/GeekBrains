from requests import get
from bs4 import BeautifulSoup

def currency_rates(currency_name):
    dict_currency = {}
    response = get(" http://www.cbr.ru/scripts/XML_daily.asp")
    soup = BeautifulSoup(response.text, "lxml")
    charcode = soup.find_all("charcode")
    value = soup.find_all("value")
    for i in range(0, len(charcode)):
        dict_currency[charcode[i].text] = float(value[i].text.replace(',', '.'))
    if currency_name.upper() in dict_currency.keys():
        return print(F" Kурс {currency_name} к рублю равен {dict_currency.get(currency_name.upper())}")
    else:
        return print("Нет информации по данной монете")

if __name__ == '__main__':
    currency_rates("eur")
    currency_rates("USD")