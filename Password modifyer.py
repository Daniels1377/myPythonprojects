word = input()
password = ''

replace_char = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}

for key, value in replace_char.items():
    word = word.replace(key,value)
print(word + 'q*s')