# Урок 1. Знакомство с Python

# задача 2 - branch two. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print("Input X: ")
# x = int(input())
# print("Input Y: ")
# y = int(input())
# print("Input Z: ")
# z = int(input())

numbers = [0, 1]
for i in numbers:
    x = i
    for e in numbers:
        y = e
        for u in numbers:
            z = u
            left_side = not(x or y or z)
            right_side = not(x) and not(y) and not(z)
            if left_side == right_side:
                print(True)
            else:
                print(False)

