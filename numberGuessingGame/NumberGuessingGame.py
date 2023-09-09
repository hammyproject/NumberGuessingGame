import random
import time

def game_start():
    playerName = input('What is your name? ')
    print(f'Hello {playerName}! Welcome to the Python Number Guessing Game!')
    return playerName

def get_level():
    level = input('Difficulty level: easy or hard. ')
    return level

def easy_game():
    random_number = random.randint(1, 100)
    guesses = 10
    n = guesses
    print('I am thinking of a number between 1 and 100.')
    print('Can you guess the number in ' + str(guesses) + ' tries?')

    for i in range(guesses):
        guess = input('Enter a number between 1 and 100: ')
        n = n - 1
        if int(guess) == random_number:
            print('You guessed correctly!')
            break
        if int(guess) > random_number:
            print('You guessed too high!')
        if int(guess) < random_number:
            print('You guessed too low!')

        if n == 1:
            print('Try again! You have ' + str(n) + ' more guess.')
        elif n != 0:
            print('Try again! You have ' + str(n) + ' guesses left!')
        else:
            print('Game over! You have no more guesses left!')
            print('The number was ' + str(random_number))
            break

def hard_game():
    random_number = random.randint(1, 100)
    guesses = 5
    n = guesses
    print('I am thinking of a number between 1 and 100.')
    print('Can you guess the number in ' + str(guesses) + ' tries?')

    for i in range(guesses):
        guess = input('Enter a number between 1 and 100: ')
        n = n - 1
        if guess == str(random_number):
            print('You guessed correctly!')
            break
        if int(guess) > random_number:
            print('You guessed too high!')
        if int(guess) < random_number:
            print('You guessed too low!')

        if n == 1:
            print('Try again! You have ' + str(n) + ' more guess.')
        elif n != 0:
            print('Try again! You have ' + str(n) + ' guesses left!')
        else:
            print('Game over! You have no more guesses left!')
            print('The number was ' + str(random_number))
            break

game_start()
level = get_level()
if level == 'easy':
    easy_game()
if level == 'hard':
    hard_game()