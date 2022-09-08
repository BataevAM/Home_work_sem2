# Задайте список из k чисел последовательности
#  (1 + 1/k)^k и выведите на экран их сумму.

n = int(input("Задайте количество чисел в списке: "))

def numbers(n):
    summ = 0
    for i in range(n):
        k = int(input(f"Введите число № {i + 1}: "))
        k = (1+1/k)**k
        summ = k + summ
        i += 1
    return summ

print("Сумма всех заданных чисел равна",round((numbers(n)), 2))