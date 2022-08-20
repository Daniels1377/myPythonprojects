name = input('Enter your name ')
import random
print('Welcome to the higher/lower game,', name)
low = int(input('Enter the lower bound: '))
high = int(input('Enter the upper bound: '))

while low > high:
    print('The lower bound must be less than the upper bound. \n')
    low = int(input('Enter the lower bound: '))
    high = int(input('Enter the upper bound: '))

correct_num = random.choice(range(low, high))
print()
print('Great, now guess a number between', low, 'and', high, end='')
guess = int(input(': '))
while guess != correct_num:
    if correct_num > guess:
        print('Nope, too low. \n')
        guess = int(input('Guess another number: '))
    elif correct_num < guess:
        print('Nope, too high. \n')
        guess = int(input('Guess another number: '))
print('You got it!')


