first_sentence = input()
second_sentence = input()

first = first_sentence.split('  ')
my_dict = dict(i.split() for i in first)
second = second_sentence.split()

for s, value in my_dict.items():
    while s in second:
       index = second.index(s)
       second[index] = value

print(' '.join(second))
