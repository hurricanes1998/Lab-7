arr = [1, 3, 5, 7, 9]
chislo = int(input("Введите число: "))

if chislo in arr:
    print("Исходный список: ", arr)
    print("Число пользователя: ", chislo)
    print("Вы угадали число!")
else:
    print("Исходный список: ", arr)
    print("Число пользователя: ", chislo)
    print("Такого числа нет")