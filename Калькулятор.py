import math
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степнь")
print("6. Извлечение квадратного корня")
print("7. Факториал")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")
a = input('Какую операцию хотите провести? ')
if a.isdigit():
    a = int(a)
else:
    print("Введите целое число от 1 до 10")
match a:
    case 1:
        print("Введите два числа. ")
        raz=input("Первое: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Первое: ")
        dva=input("Второе: ")
        while type(dva) != float:
         try:
            dva=float(dva)
         except ValueError:
            print("Введите число")
            dva=input("Второе: ")
        sum=raz+dva
        print("Сумма равна: ", sum)
    case 2:
        print("Введите два числа. ")
        raz=input("Первое: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Первое: ")
        dva=input("Второе: ")
        while type(dva) != float:
         try:
            dva=float(dva)
         except ValueError:
            print("Введите число")
            dva=input("Второе: ")
        sum=raz-dva
        print("Разность равна: ", sum)
    case 3:
        print("Введите два числа. ")
        raz=input("Первое: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Первое: ")
        dva=input("Второе: ")
        while type(dva) != float:
         try:
            dva=float(dva)
         except ValueError:
            print("Введите число")
            dva=input("Второе: ")
        sum=raz*dva
        print("Произведение равно: ", sum)
    case 4:
        print("Введите два числа. ")
        raz=input("Первое: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Первое: ")
        dva=input("Второе: ")
        while type(dva) != float:
          try:
            dva=float(dva)
          except ValueError:
            print("Введите число")
            dva=input("Второе: ")
        if dva == 0:
         print("На ноль делить нельзя.")
        else:
         sum=raz/dva
         print("Частное: ", sum)
    case 5:
        print("Введите число и степень.")
        raz=input("Число: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Число: ")
        dva=input("Степень: ")
        while type(dva) != float:
         try:
            dva=float(dva)
         except ValueError:
            print("Введите число")
            dva=input("Степень: ")
        sum=raz**dva
        print("Число ",raz," в степени ",dva, " = ",sum)
    case 6:
        raz=input("Введите число: ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Число: ")
        if raz >= 0:
         sum=raz**0.5
         print("Корень равен: ", sum)
        else:
           print("Корня из отрицательного числа не существует.")
    case 7:
        raz=input("Введите число: ")
        while type(raz) != int:
         try:
            raz=int(raz)
         except ValueError:
            print("Введите целое число")
            raz=input("Число: ")
            raz=int(raz)
         from math import factorial
         sum=factorial(raz)
         print("Факториал равен: ", sum)
    case 8:
        raz=input("Введите угол. ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Число: ")
         sum=float(math.sin(raz))
         print("Синус равен: ", sum)
    case 9:
        raz=input("Введите угол. ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Число: ")
         sum=float(math.cos(raz))
         print("Косинус равен: ", sum)
    case 10:
        raz=input("Введите угол. ")
        while type(raz) != float:
         try:
            raz=float(raz)
         except ValueError:
            print("Введите число")
            raz=input("Число: ")
         sum=float(math.tan(raz))
         print("Тангенс равен: ", sum)