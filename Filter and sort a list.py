number = list(map(int,input().split(' ')))
number.sort()
for num in number:
    if num >= 0:
        print(num, end = ' ')