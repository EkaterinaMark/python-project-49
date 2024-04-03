import random

def sum_num(a, b):
    return a + b
    
    
def mult_num(a, b):
    return a * b
    
    
def diff_num(a, b):
    return a - b
    
    
list_of_functions = [sum_num, mult_num, diff_num]
list_of_operations = ['+', '*', '-']

first_number = random.randint(1, 100)
second_number = random.randint(1, 100)
operation_number = random.randint(0, 2)

correct_answer = list_of_functions[operation_number](first_number, second_number)

print('Question: ', first_number, list_of_operations[operation_number], second_number)
print(correct_answer, operation_number)