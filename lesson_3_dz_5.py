import random
from random import choice
def get_jokes(n):
    """made a random list of jokes"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(n):
        one = random.choice(nouns)
        two = random.choice(adverbs)
        three = random.choice(adjectives)
        joke = f"{one} {two} {three}"
        print(joke)
get_jokes(1)
get_jokes(1)
get_jokes(1)
get_jokes(1)