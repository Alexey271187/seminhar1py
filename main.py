"""Задача 2: Найдите сумму цифр трехзначного числа."""
"""number = int(input('Введите трехзначное число:'))
a = number // 100
b = number // 10 % 10
c = number % 10
print((a + b + c))"""

"""Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"""
"""s = int(input('Введите сколько журавликов сделали дети:'))
print((s//6), ((s//6)*4), (s//6))"""

"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета."""
"""number = input('Введите номер билета:')
s1 = int(number[0]) + int(number[1]) + int(number[2])
s2 = int(number[3]) + int(number[4]) + int(number[5])
if s1 != s2:
    print('no')
else:
    print('yes')"""

"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)"""
"""n = int(input('Введите сколько долек длинна шоколадки:'))
m = int(input('Введите сколько долек ширина шоколадки:'))
k = int(input('На сколько частей хотим поделить:'))
if k < m*n and (k%m==0 or k%n==0):
    print('Так можно поделить на 2 прямоугольника')
else:
    print('Так нельзя поделить на 2 прямоугольника')"""

"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть"""

"""n = int(input('Введите кол-во монеток: '))
print('Разложте монетки на столе:')
print('1 это орел, 0 это решка')
tails = 0
for i in range(n):
    eagle = int(input())
    if eagle == 1:
       tails += 1
print('Нужно перевернуть: ', tails if tails < n / 2 else n - tails)"""

"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа."""

"""sum_numbers = int(input('Введите сумму 2-х загаданных чисел: '))
product_numbers = int(input('Введите произведение 2-х загаданных чисел: '))
for i in range(0,sum_numbers):
    for j in range(0,product_numbers):
        if i * j == product_numbers:
            if i + j == sum_numbers:
                print(i, j)
            else:
                print('error')
"""
"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

"""n = int(input('Введите число N: '))
i = 1
while i < n:
    print(i, end=' ')
    i *= 2"""

"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X"""

list_1 = []
n = int(input('На сколько элементов сделаем массив? '))
for i in range(n):
    a = int(input('Введите значение элемента  '))
    list_1.append(a)
print(list_1)
x = int(input('Какое число ищем в массиве '))
print(str(f'Число {x} встречается в массиве'),len([elem for elem in list_1 if elem == x]), str('раз.'))

"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X"""

list_1 = []
n = int(input('На сколько элементов сделаем массив? '))
for i in range(n):
    a = int(input('Введите значение элемента  '))
    list_1.append(a)
print(list_1)
x = int(input('Какое число ищем в массиве '))
list_2 =[]
for j in range(n):
    list_2.append(abs(x - list_1[j]))
y = (list_2.index(min(list_2)))
print(str(f'Ближайшее число к {x} это {list_1[y]}'))

"""Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
либо только русские буквы."""

points = {
    1:'АВЕИНОРСТ',
    2:'ДКЛМПУ',
  	3:'БГЁЬЯ',
  	4:'ЙЫ',
    5:'ЖЗХЦЧ',
    8:'ШЭЮ',
    10:'ФЩЪ'}
print('Поиграем в Скрабл')
text = input('Введите слово: ').upper()
count = 0
for i in text:
  if i in 'АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ':
    for j in points:
      if i in points[j]:
        count +=j
print(f'За слово {text} вы получаете {count} баллов.')
