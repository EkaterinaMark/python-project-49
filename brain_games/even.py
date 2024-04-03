import random


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    number = random.randint(1, 100)
    return number
    

def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
