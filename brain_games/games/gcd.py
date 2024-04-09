import random


description = 'Find the greatest common divisor of given numbers.'


def elements():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    return (first_number, second_number)
    

def question(element_tuple):
    expression = str(element_tuple[0]) + ' ' + str(element_tuple[1])
    return expression


def correct_answer(element_tuple):
    a, b = element_tuple
    if a < b:
        a, b = b, a
    mod = a % b
    while mod != 0:
        a, b = b, mod
        mod = a % b
    return b
