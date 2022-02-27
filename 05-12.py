##Proc16. Описать функцию Sign(X) целого типа, возвращающую для вещественного
##числа X следующие значения: −1, если X < 0; 0, если X = 0; 1, если X > 0.
##С помощью этой функции найти значение выражения Sign(A) + Sign(B) для данных
##вещественных чисел A и B.
##def sign(x):
##    s = 0
##    if x < 0:
##        s = -1
##    elif x == 0:
##        s = 0
##    elif x > 0:
##        s = 1
##    return s
##
##a = float(input())
##b = float(input())
##print(sign(a) + sign(b))

##Proc17. Описать функцию RootsCount(A, B, C) целого типа, определяющую
##количество корней квадратного уравнения A·x2 + B·x + C = 0
##(A, B, C — вещественные параметры, A != 0). С ее помощью найти количество корней
##для каждого из трех квадратных уравнений с данными коэффициентами. Количество
##корней определять по значению дискриминанта: D = B^2 −4·A·C.

##def roots_count(a,b,c):
##    d = b**2 - 4 * a * c
##    h = 0
##    if d > 0:
##       h = 2
##    elif d == 0:
##       h = 1
##    elif d < 0:
##       h = 0
##    return h
##
##a = float(input())
##b = float(input())
##c = float(input())
##print(roots_count(a,b,c))

##def circle_s(r):
##    return 2 * 3.14 * r**2
##
##i=1
##while i <= 3:
##    r = float(input())
##    print(circle_s(r))
##    i = i + 1

##Proc19. Описать функцию RingS(R1, R2) вещественного типа, находящую площадь
##кольца, заключенного между двумя окружностями с общим центром и радиусами R1 и
##R2 (R1 и R2 — вещественные, R1 > R2). С ее помощью найти площади трех колец,
##для которых даны внешние и внутренние радиусы. Воспользоваться формулой
##площади круга радиуса R: S = π·R2. В качестве значения π использовать 3.14. 

##def ring_s(r1,r2):
##    s1 = 3.14*r1*r1
##    s2 = 3.14*r2*r2
##    return s1-s2
##
##i=1
##while i <= 3:
##    r1 = float(input())
##    r2 = float(input())
##    print(ring_s(r1,r2))
##    i = i + 1

##def sum_range(a,b):
##    summ = 0
##    i = a
##    while i <= b:
##        summ += i
##        i += 1
##    return summ

#=============СПИСКИ================
##import random
##students = ["Гарри", "Гермиона", "Драко", "Рон", "Невил", "Луна"]
##griffindor = []
##slizerin = []
##
##i=1
##while i <= 3:
##    stud = random.choice(students)
##    griffindor.append(stud) # добавили переменную в список
##    students.remove(stud) # удалили переменную из списка
##    i = i + 1
##print("Гриффиндор", griffindor)
##
##
##slizerin.extend(students) # добавили список в список
##print("Слизерин", slizerin)

#=====Крестики-нолики=====
def init_field(field):
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        field.append(row)

def print_field(field):
    for i in range(3):
        print("|---"*3,end='')
        print('|')
        for j in range(3):
            print('| ' + field[i][j]+ ' ',end='')
        print('|')
    print("|---"*3,end='')
    print('|')

def take_input(field):
    print("введите номер строки и номер столбца")
    row = int(input())
    col = int(input())
    print("введите отметку x или о")
    s = input()
    field[row][col] = s

def check_win(field, sign):
    #проверка строк
    if field[0][0] == sign and field[0][1] == sign and field[0][2] == sign:
        return True
    if field[1][0] == sign and field[1][1] == sign and field[1][2] == sign:
        return True
    if field[2][0] == sign and field[2][1] == sign and field[2][2] == sign:
        return True
    #проверка столбцов
    if field[0][0] == sign and field[1][0] == sign and field[2][0] == sign:
        return True
    if field[0][1] == sign and field[1][1] == sign and field[2][1] == sign:
        return True
    if field[0][2] == sign and field[1][2] == sign and field[2][2] == sign:
        return True
    #проверка главной диагонали
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return True
    #проверка побочной диагонали
    if field[0][2] == sign and field[1][0] == sign and field[2][0] == sign:
        return True
    
def check_draw(field):
    k = 0
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                k += 1
    if k == 0:
        return True
    else:
        return False

field=[]
init_field(field)
while True:
    take_input(field)
    print_field(field)
    #проверить на победу
    if check_win(field, 'x'):
        print("Выиграли крестики")
        break
    #проверить на ничью
    if check_draw(field):
        print("Ничья")
        break

    take_input(field)
    print_field(field)
    #проверить на победу
    if check_win(field, 'o'):
        print("Выиграли нолики")
        break
    #проверить на ничью
    if check_draw(field):
        print("Ничья")
        break

















