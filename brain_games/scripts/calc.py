import random

description = 'What is the result of the expression?'


def elements():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    return (first_number, second_number, operation)
    

def question(element_tuple):
    expression = str(element_tuple[0]) + ' ' + element_tuple[-1] + ' ' + str(element_tuple[1])
    return expression
    
    
def correct_answer(element_tuple):
    if element_tuple[-1] == '+':
        return element_tuple[0] + element_tuple[1]
    elif element_tuple[-1] == '-':
        return element_tuple[0] - element_tuple[1]
    else:
        return element_tuple[0] * element_tuple[1]