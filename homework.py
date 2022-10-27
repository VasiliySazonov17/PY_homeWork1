# Урок 1. Знакомство с Python
# задача 3 - branch three. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3



def check_plane (x, y):
    if x > 0 and y > 0:
        print('1')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:  
        print('3')
    else:
        print('4')

print("Input x: ")
x = int(input())
print("Input y: ")
y = int(input())
check_plane (x, y)