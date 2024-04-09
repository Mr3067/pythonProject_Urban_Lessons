totle = 0
count_err = 0
str_N = 0
with open('calc.txt', 'r') as f:
    for i in f:
        str_N += 1
        try:
            totle += eval(i)
            print(totle)
        except SyntaxError as err:
            count_err += 1
            print(f'Ошибка №{count_err} тип \"{err}\" в строке \"{i[:-1]}\" номер строки в файле {str_N}')

print(totle)

# 401380012.946437
