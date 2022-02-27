import random
## Игра Кости
##c = 'y'
##while c == 'y':
##    ## Ход 1-го игрока
##    cube1 = random.randint(1,6) # выдать случайное целое от 1 до 6
##    cube2 = random.randint(1,6)
##    player_1_score = cube1 + cube2
##    print("Первый игрок выбросил", cube1, cube2, "сумма", player_1_score)
##    ## Ход 2-го игрока
##    cube1 = random.randint(1,6) # выдать случайное целое от 1 до 6
##    cube2 = random.randint(1,6)
##    player_2_score = cube1 + cube2
##    print("Второй игрок выбросил", cube1, cube2, "сумма", player_2_score)
##    ## Анализ кто победил или ничья
##    if player_1_score > player_2_score:
##        print("Победил первый")
##    elif player_2_score > player_1_score:
##        print("Победил второй")
##    elif player_1_score == player_2_score:
##        print("Ничья")
##    print("Хотите сыграть ещё? Нажмите англ. y  если да, любую другую клавишу если нет")
##    c = input()

## Игра "Камень-ножницы-бумага"

##def translate(number):
##    if number == 1:
##        choice = 'камень'
##    elif number == 2:
##        choice = 'ножницы'
##    elif number == 3:
##        choice = 'бумага'
##    return choice
##
##
##    
##c = 'y'
##while c == 'y':
##    comp = random.randint(1,3)
##    
##    comp_choice = translate(comp)
##    
##    print("Ваш ход. \nЧтобы выбрать камень - нажмите клавишу 1")
##    print("Чтобы выбрать ножницы - нажмите клавишу 2")
##    print("Чтобы выбрать бумагу - нажмите клавишу 3")
##    player = int(input())
##
##    player_choice = translate(player)
##
##    print("Компьютер загадал", comp_choice)
##    print("Игрок загадал", player_choice)
##    # Проверка на ничью
##    if player_choice == comp_choice:
##        print("Ничья")
##    # Проверка на победу игрока
##    if player_choice == 'камень' and comp_choice == 'ножницы':
##        print("Победил игрок")
##    if player_choice == 'ножницы' and comp_choice == 'бумага':
##        print("Победил игрок")
##    if player_choice == 'бумага' and comp_choice == 'камень':
##        print("Победил игрок")    
##    # Проверка, что победил комп
##    if comp_choice == 'камень' and player_choice == 'ножницы':
##        print("Победил компьютер")
##    if comp_choice == 'ножницы' and player_choice == 'бумага':
##        print("Победил компьютер")
##    if comp_choice == 'бумага' and player_choice == 'камень':
##        print("Победил компьютер") 
##    print("Хотите сыграть ещё? Нажмите англ. y  если да, любую другую клавишу если нет")
##    c = input()

##=======================ФУНКЦИИ==============================
#Proc1. Описать функцию PowerA3(A, B), вычисляющую третью степень числа
#A и возвращающую ее. С помощью этой функции найти третьи степени пяти данных
#чисел.

##def powerA3(a):
##    b = a*a*a
##    return b
##
### повторять 5 раз
### начальное значение счетчика
##i = 1
##while i <= 5:
##    # ввести число
##    c = int(input())
##    # вычислить и вывести его куб
##    print(powerA3(c))
##    # изменить счетчик цикла
##    i = i + 1

#Proc3. Описать 2 функции a_mean(x, y) g_mean(x, y), вычисляющую среднее
# арифметическое AMean = (X+Y)/2 и среднее геометрическое
#GMean = √X·Y двух положительных чисел X и Y
#С помощью этих функций найти среднее арифметическое и среднее геометрическое
#для трех пар чисел
##import math
##def a_mean(x, y):
##    return (x+y)/2
##
##def g_mean(x, y):
##    return math.sqrt(x*y)
##
### повторить 3 раза
### начальное значение счетчика
##i = 1
##while i <= 3:
##    a = int(input())
##    b = int(input())
##    print("среднее арифметическое", a_mean(a,b))
##    print("среднее геометрическое", g_mean(a,b))
##    i = i + 1


#Proc4◦. Описать 2 функции triangle_p(a) triangle_s(a)
#вычисляющие по стороне a равностороннего треугольника его периметр P=3·a
# и площадь S = a^2·√3/4. С помощью этих ф-ций вычислить для 4х треугольников
##import math
##def triangle_p(a):
##    return 3*a
##
##def triangle_s(a):
##    return a**2 * math.sqrt(3) / 4
##
##i = 1
##while i <= 4:
##    print("Введите сторону равностороннего треугольника")
##    a = int(input)
##    print("периметр", trinagle_p(a))
##    print("площадь", trinagle_s(a))

def rect_p(x1, y1, x2, y2):
    a = abs(y1-y2)
    b = abs(x1-x2)
    return 2*(a+b)

def rect_s(x1, y1, x2, y2):
    a = abs(y1-y2)
    b = abs(x1-x2)
    return a*b

i = 1
while i <= 3:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print("периметр", rect_p(x1,y1,x2,y2))
    print("площадь", rect_s(x1,y1,x2,y2))
    i = i + 1
