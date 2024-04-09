#!/usr/bin/env python3
import prompt
from brain_games.games import gcd


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
        elements = game.elements()
        question = game.question(elements)
        correct_answer = str(game.correct_answer(elements))
        print('Question:', question)
        print('Your answer: ', end='')
        user_answer = str(input())
        if user_answer == correct_answer:
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
    game_description(gcd)
    game_session(gcd, user_name)


if __name__ == '__main__':
    main()
