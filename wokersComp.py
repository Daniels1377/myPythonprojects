user_hours = float(input())

if (0 < user_hours <= 40):
    (avg_pay) = (user_hours * 20)
    print('$' + '{:.2f}'.format(avg_pay))
elif (168 >= user_hours > 40):
    user_hours1 = (user_hours % 40)
    avg_hours = (user_hours - user_hours1)
    avg_pay = (avg_hours * 20)
    ovt_hours = (user_hours1 * 30)
    total_pay = (avg_pay + ovt_hours)
    print('$' + '{:.2f}'.format(total_pay))
else:
    print('Invalid')