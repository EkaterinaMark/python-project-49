#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
    

#определяет верный ответ на вопрос
def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for _ in range(3):
        number = random.randint(1, 100)
        print('Question:', number)
        print('Your answer: ', end = '')
        user_answer = input()
        if  user_answer == correct_answer(number):
            print('Correct!')
            count += 1
        else:
            print("'" + user_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + correct_answer(number) + "'")
            print(f"Let's try again, {user_name}!")            
            break
    if count == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()        