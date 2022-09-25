#Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
x1 =  int(input('for point A, enter the X1 coordinate = '))
y1 =  int(input('for point A, enter the Y1 coordinate = '))
x2 =  int(input('for point B, enter the X2 coordinate = '))
y2 =  int(input('for point B, enter the X2 coordinate = '))
l = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
length = math.sqrt(l)
# print(length) выдает число с 15ю знаками после запятой
# print(round(math.sqrt(l)),2) округляет ровно до 9, знаки после запятой не прописывает, только само число 2
print(round(length,2))# округляет до 2 знаков после запятой
