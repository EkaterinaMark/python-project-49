import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
    
    
def game_description(game):
    print(game.description)
    
    
def game_session(game):
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
            print(f"Let's try again!")            
            break
    if count == 3:
        print('Congratulations!')

       
def main():
    user_name = welcome_user()
    game_description(game)
    game_session(game)
