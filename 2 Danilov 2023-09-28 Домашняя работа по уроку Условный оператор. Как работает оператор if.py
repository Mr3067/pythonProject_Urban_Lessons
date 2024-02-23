
# пункт 3
x = int(input('Введите целое значение x:'))
print('драути')
if x < 0:
    print('x Меньше нуля')
elif x == 0:
    print('x = 0')
else:
    print('x Больше нуля')

# _____________________________________________________________


# Пункт 4

a = input('Введите целое значение a:')
b = input('Введите целое значение b:')

while a.isdigit() and b.isdigit():

    a = int(a)
    b = int(b)

    if a > b:
        print('a > b')

    if a > b and a > 0:
        print('успех, a > b and a > 0')

    if (a > b) and (a > 0 or b < 1_000):
        print('успех, (a > b) and (a > 089 or b < 1_000)')
    if 5 < b < 10:
        print('успех, 5 < b and b < 10')
    print()

    a = input('Введите целое значение a:')
    b = input('Введите целое значение b:')

else:
    print('Введено неверное значение. Пока!')
    exit()

# _____________________________________________________________
# Пункт 5 не обнаружен

# Пункт 6

if '34' > '123':
    print('Success')
if '123' > '12':
    print('Success')
if [1,2] > [1,1]:
    print('Success')
# _____________________________________________________________

# Пункт 7

if '6' > 5:
    print('Success')

if [5,6] > 5:
    print('Success')

if '6' != 5:
    print('Success')


