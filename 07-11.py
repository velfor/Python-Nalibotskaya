# If1. Дано целое число. Если оно является положительным, то прибавить к нему 1;
# в противном случае не изменять его. Вывести полученное число.
##a = int(input())
##if a > 0:
##    a = a + 1
##print(a)

#If2. Дано целое число. Если оно является положительным, то прибавить к нему 1;
# в противном случае вычесть из него 2.Вывести полученное число. 
##a = int(input())
##if a > 0:
##    a = a + 1
##else:
##    a = a - 2
##print(a)

# If3. Дано целое число. Если оно является положительным, то прибавить к нему 1;
# если отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Вывести полученное число.
##a = int(input())
##if a > 0:
##    a = a + 1
##elif a < 0:
##    a = a - 2
##elif a == 0:
##    a = 10
##print(a)

# If4. Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.
##print("Введите 3 целых числа")
##a = int(input())
##b = int(input())
##c = int(input())
##kol = 0
##if a > 0:
##    kol = kol + 1
##if b > 0:
##    kol = kol + 1
##if c > 0:
##    kol = kol + 1
##print("Количество положительных чисел",kol)

# If5. Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе. 
##print("Введите 3 целых числа")
##a = int(input())
##b = int(input())
##c = int(input())
##kol_pol = 0
##if a > 0:
##    kol_pol = kol_pol + 1
##if b > 0:
##    kol_pol = kol_pol + 1
##if c > 0:
##    kol_pol = kol_pol + 1
##
##kol_otr = 0
##if a < 0:
##    kol_otr += 1
##if b < 0:
##    kol_otr += 1
##if c < 0:
##    kol_otr += 1
##print("Количество положительных чисел",kol_pol)
##print("Количество отрицательных чисел",kol_otr)

#If6◦. Даны два числа. Вывести большее из них.
##a = int(input())
##b = int(input())
##if a > b:
##    print(a)
##elif b > a:
##    print(b)
##elif a == b:
##    print("Числа равны")

#If7. Даны два числа. Вывести порядковый номер меньшего из них.
##a = int(input())
##b = int(input())
##if a < b:
##    print(1)
##elif b < a:
##    print(2)
##elif a == b:
##    print("Числа равны")

#If8◦. Даны два числа. Вывести вначале большее, а затем меньшее из них. 
##a = int(input())
##b = int(input())
##if a > b:
##    print(a,b)
##elif b > a:
##    print(b,a)
##elif a == b:
##    print("Числа равны")

# If9. Даны две переменные вещественного типа: A, B. Перераспределить значения
# данных переменных так, чтобы в A оказалось меньшее из значений, а в B — большее.
# Вывести новые значения переменных A и B.
##a = float(input())
##b = float(input())
##if a > b:
##    c = b
##    b = a
##    a = c
##    # a,b = b,a
##print(a,b)

# If10. Даны две переменные целого типа: A и B. Если их значения не равны,
#то присвоить каждой переменной сумму этих значений, а если равны, то присвоить
#переменным нулевые значения. Вывести новые значения переменных A и B.
##a = int(input())
##b = int(input())
##if a != b:
##    summa = a + b
##    a = summa
##    b = summa
##else:
##    a = 0
##    b = 0
##print(a,b)

# If11. Даны две переменные целого типа: A и B. Если их значения не равны,
# то присвоить каждой переменной большее из этих значений, а если равны,
# то присвоить переменным нулевые значения. Вывести новые значения переменных
# A и B.
##a = int(input())
##b = int(input())
##if a != b:
##    if a > b:
##        b = a
##    if b > a:
##        a = b
##elif a == b:
##    a = b = 0
##print(a,b)

#If12◦. Даны три числа. Найти наименьшее из них
##a = float(input())
##b = float(input())
##c = float(input())
##minimum = a
##if b < minimum:
##    minimum = b
##if c < minimum:
##    minimum = c
##print(minimum)

#If24. Для данного вещественного x найти значение следующей функции f,
###принимающей вещественные значения: f(x) = 2·sin(x), если x > 0, 6−x, если x ≤ 0.
##x = float(input())
##if x > 0:
##    y = 2*x
##elif x <= 0:
##    y = 6 - x
##print(y)

##If26 ◦. Для данного вещественного x найти значение следующей функции f,
##принимающей вещественные значения: −x, если x ≤ 0,f (x) = x^2, если 0 < x < 2,
##4, если x ≥ 2
##x = float(input())
##if x <=0:
##    y = -x
##elif 0 < x < 2:
##    y = x ** 2
##elif x >= 2:
##    y = 4

##If28 . Дан номер года (положительное целое число). Определить количество дней
##в этом году, учитывая, что обычный год насчитывает 365 дней,
##а високосный — 366 дней. Високосным считается год, делящийся на 4,
##за исключением тех годов, которые делятся на 100 и не делятся на 400
##(например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 —
## являются). 
##god = int(input())
##if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
##    print(366)
##else:
##    print(365)
#Case1. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
#соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т.д.).
day = int(input())
if day == 1:
    print("понедельник")
elif day == 2:
    print("вторник")


else:
    print("Ошибка")





