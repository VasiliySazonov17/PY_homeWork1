# Урок 1. Знакомство с Python
# задача 1 - branch one. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#  Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 

def check_weekends(x):
    weekday = ['1', '2', '3', '4', '5']
    weekends = ['6', '7']
    
    for i in weekday:
        if x == i:
            print("No")
        
    for i in weekends:
        if x == i:
            print("Yes")


print("Input number: ")
y = input()
check_weekends(y)




