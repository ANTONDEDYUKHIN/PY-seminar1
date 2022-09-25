#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
n = int(input('enter an integer N = '))
if n==6 or n==7:
    print('Yes: this day is a weekend')
elif n<1 or n>7:
    print('Enter correct integer!')
else:
    print('No: It is a working day')
