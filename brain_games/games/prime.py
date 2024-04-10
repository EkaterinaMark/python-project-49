import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    number = random.randint(2, 100)
    return number


def correct_answer(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'
