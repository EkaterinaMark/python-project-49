#!/usr/bin/env python3
import prompt
#import even
from brain_games.games import even


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
    
    
def game_description(game):
    print(game.description)
    
   
def game_session(game, name):
    count = 0
    for _ in range(3):
        question = game.question()
        correct_answer = game.correct_answer(question)
        print('Question:', question)
        print('Your answer: ', end = '')
        user_answer = input()
        if  user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print("'" + user_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + correct_answer + "'")
            print(f"Let's try again, {name}!")            
            break
    if count == 3:
        print(f'Congratulations, {name}!')

       
def main():
    user_name = welcome_user()
    game_description(even)
    game_session(even, user_name)
    
if __name__ == '__main__':
    main()
'''
name = welcome_user()
game_description(even)
current_question = even.question()
print('Question: ', current_question)
correct_answer = even.correct_answer(current_question)
print('Your answer: ', end = '')
user_answer = input()
print(correct_answer, user_answer)
'''