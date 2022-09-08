# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

def InputNumbers(inputText):
    correct = False
    while not correct:
        try:
            number = float(input(f"{inputText}"))
            correct = True
        except ValueError:
            print("Это не число! Используйте 'точку' в качестве разделителя.")
    return number


def summNumbers(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите целое или вещественное число: ")

print(f"Сумма цифр в данном числе равна = {summNumbers(num)}")