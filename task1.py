#напишите программу, которая принимает на вход 2 числа и проверяет
#является ли 1 число квадратом другого. 5, 25 - да, 8,9 - нет
print('input number a = ')
a =  int(input())
print('input number b = ')
b =  int(input())
if a*a == b:
    print('Yes')
else:
    print('No')
