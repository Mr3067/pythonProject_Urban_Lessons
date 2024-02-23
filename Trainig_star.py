# a, *b, c = [1, 4, 6, 'fdsg', 56, 'dsfs']
# print(a, b, c)
#
# s = [3, 20, 3]
# print(list(range(*s)))

# m = (2, 3, 4, 'sep = u', 'end = OOO')
# print(*m)
# z = {*m}
# print(z)

# def word_cut(_my_str):
#     if len(_my_str) == 1 or len(_my_str) == 2:
#         return _my_str
#     return _my_str[0] + '(' + word_cut(_my_str[1:-1]) + ')' + _my_str[-1]
#
# print(word_cut('jkhdfssjkflhajhfj'))

# #Фибонначи
# def fun_1(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fun_1(n - 1) + fun_1(n-2)
#
#
# print(fun_1(10))

# # Факториал
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(10))

# # Палиндром
# def palin(_in_str):
#     if len(_in_str) == 1 or _in_str == '':
#         return True
#     if _in_str[0] == _in_str[-1]:
#         return palin(_in_str[1:-1])
#     return False
#
#
#
# a = ['radar', 'banana', 'hannah', 'pup' ,'nan', 'lollipop', 'eye', '6543456', 'deed']
# for i in a:
#     print(palin(i))

# # Задание из видео https://www.youtube.com/watch?v=rzGCxtZdMuM на 5:48
# def penta(int_snr):
#     if len(int_snr) == 1:
#         return int_snr
#     return int_snr[0] + '*' + penta(int_snr[1:])
#
# print(penta('asdsasda'))

# # Задача https://informatics.msk.ru/mod/statements/view3.php?id=26735&chapterid=113657#1
# def make_symm(_in_str):
#     if len(_in_str) == 1:
#         if _in_str[0] == '(':
#             return '()'
#         return _in_str + _in_str
#     if _in_str[0] == '(':
#         return '(' + make_symm(_in_str[1:]) + ')'
#     else:
#         return _in_str[0] + make_symm(_in_str[1:]) + _in_str[0]
#
# print(make_symm('(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo') == '(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqooqk))r)m))p)xs))s))imu)d)ktm))))))))y)d))))s))xlm)h)))m)v))e)v))wv)))))))e))))xk))y))p))t)))')
# print()

# def make_symm_rev(_in_str):
#     if len(_in_str) == 1:
#         if _in_str[0] == '(':
#             return '()'
#         return _in_str+_in_str
#     if _in_str[-1] == ('('):
#         return '(' + make_symm_rev(_in_str[:-1]) + ')'
#
#     return _in_str[-1] + make_symm_rev(_in_str[:-1]) + _in_str[-1]
#
#
# a = '(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo'
# print(a)
# print(make_symm_rev(a))

# # Возведение в степень
# # https://www.youtube.com/watch?v=rzGCxtZdMuM 7:54
# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1/(power(x,-n))
#     if n % 2 ==  0:
#         return power(x,(n//2))*power(x,(n//2))
#     return power(x,(n-1))*x
#
#
# print(power(5, -2))

# # Обход вложенных структур
# # https://www.youtube.com/watch?v=rzGCxtZdMuM 10:38
#
# def go_around(_in_list, level = 1):
#     print(*_in_list, 'Level', level)
#     for i in _in_list:
#         if type(i) == list:
#             go_around(i, level+1)
#
#
#
# a = [11,[22,26,29],12,13,[25,26,[36,39,[40,44,46],37,35],27]]
#
# go_around(a)

# #Обход файлов https://www.youtube.com/watch?v=wZvk8nyPQCY
# import os
#
# def obxod(path, level = 1):
#     print('Level = ', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\'+i):
#             print('Down', path + '\\'+i)
#             obxod(path + '\\'+i, level + 1)
#             print('Return', path)
#
#     return
#
# path_Z = 'C:\\Users\\danil\\OneDrive\\Дом Коненкова (проекты)\\2024'
# print(obxod(path_Z))

# def _solve_factorial(n):
#     # if n <= 0:
#     #     print('неверное значение')
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     if n == -1:
#         return -1
#     if n < -1:
#         return n * rec(n + 1)
#     return n*rec(n-1)
#
# print(_solve_factorial(1))

def go_by_levels(_in_list, level=1):
    print(*_in_list,'level = ', level)
    for i in _in_list:
        if type(i) == list:
            go_by_levels(i, level+1)


a = [1,2,3,[22,23,[31,32,33,[41,42,43],34],24,25],4,5,[26,27,[35,36,37,38],28],6,7,8]
go_by_levels(a)


