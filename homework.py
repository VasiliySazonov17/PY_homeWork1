# Урок 1. Знакомство с Python
# задача 1 - branch one. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#  Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 

print("Input number: ")
i = input()


def check_weekends(x):
    weekday = ['1', '2', '3', '4', '5']
    weekends = ['6', '7']

    for x in weekday[i]:
        if x == weekday[i]:
            print("No")
        elif x == weekends[i]:
            print("Yes")
        else:
            print("")
    
check_weekends(i)


