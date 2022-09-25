# Написать программу, которая будет принимать на вход 
# дробное число и проверяет, кратно ли оно 5, 10 и 15, но не 30
a =  int(input('enter a number = '))
if a%5==0 and (a%10==0 or a%15==0) and a%30 !=0:
    print('Yes: divisible by 5, 10 and 15')
else:
    print('this is not diviseble by 30')