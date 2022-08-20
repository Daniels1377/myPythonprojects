user_text = input()
user_commas = user_text.count(',')
user_space = user_text.count(' ')
user_period = user_text.count('.')

user_length = len(user_text)

user_char = user_length - (user_commas + user_space + user_period)

print(user_char)