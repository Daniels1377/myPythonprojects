#user inputs name
userName = input('What is your name? \n')
userAge = int(input('How old are you? \n'))

#users age deducted by year
userYear = (2020 - userAge)
print('\nHello', userName + '!', 'You were born in', int(userYear))