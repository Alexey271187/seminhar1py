number = int(input('Введите трехзначное число:'))
a = number // 100
b = number // 10 % 10
c = number % 10
print((a + b + c))

s = int(input('Введите сколько журавликов сделали дети:'))
print((s//6), ((s//6)*4), (s//6))

number = input('Введите номер билета:')
s1 = int(number[0]) + int(number[1]) + int(number[2])
s2 = int(number[3]) + int(number[4]) + int(number[5])
if s1 != s2:
    print('no')
else:
    print('yes')

n = int(input('Введите сколько долек длинна шоколадки:'))
m = int(input('Введите сколько долек ширина шоколадки:'))
k = int(input('На сколько частей хотим поделить:'))
if k < m*n and (k%m==0 or k%n==0):
    print('Так можно поделить на 2 прямоугольника')
else:
    print('Так нельзя поделить на 2 прямоугольника')