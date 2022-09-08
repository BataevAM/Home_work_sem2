# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных 
# пользователем через пробел позициях.

from random import Random, randint


N = int(input("Введите количество элементов в списке: "))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N))
    
print("Список: ", numbers)

num1,num2 = map(int, input \
    ("ЧЕРЕЗ ПРОБЕЛ, введите порядковые номера ДВУХ чисел из списка, которые желаете перемножить: ").split())
print("Произведение: ", numbers[num1-1] * numbers[num2-1])