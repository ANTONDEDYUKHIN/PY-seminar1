# напишите программу, для подготовки к экзамену Рон каждый день учит Х заклинаний 
# Гермиона на У заклинаний больше. Сколько заклинаний они выучат через П дней?
# в 1й строке вводится Х заклинаний, во второй У заклинаний

x =  int(input('Кол-во заклинаний, которое учит Рон, Х = '))

y =  int(input('На какое кол-во заклинаний больше учит Гермиона, У = '))

n =  int(input('Кол-во дней, n = '))
print(f'Кол-во заклинаний всего за n-дней = {((x+y)+x)*n}')