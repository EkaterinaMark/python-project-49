import random


description = 'What number is missing in the progression?'


def elements():
    start = random.randint(1, 20)
    step = random.randint(2, 33)
    index = random.randint(0, 9)
    progression = [str(start)]
    next_elem = start
    for _ in range(9):
        next_elem += step
        progression.append(str(next_elem))
    return (progression, index, progression[index])
    

def question(element_tuple):
    element_tuple[0][element_tuple[1]] = '..'
    expression = ' '.join(element_tuple[0])
    return expression
    
    
def correct_answer(element_tuple):
    return element_tuple[2]