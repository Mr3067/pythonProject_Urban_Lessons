"""


"""
import inspect


def string_to_int(s):  # добавить обработку ValueError

    if isinstance(s, float):
        raise ValueError('Введено веществнное число, требуется целое')
    elif isinstance(s, str):
        raise ValueError('Введено строковое значение, требуется целое')
    elif isinstance(s, list):
        raise ValueError('Введен список, требуется целое число')
    elif isinstance(s, tuple):
        raise ValueError('Введен кортеж, требуется целое число')
    elif isinstance(s, dict):
        raise ValueError('Введен словарь, требуется целое число')
    elif not isinstance(s, int):
        raise ValueError('Введено не понятно что, требуется целое число')

    s = "Error"
    try:
        return int(s)
    except ValueError:
        print(f"Функция {inspect.getframeinfo(inspect.currentframe()).function} производит неверный рассчет")
    finally:
        print(f"!!!!!Функция {inspect.getframeinfo(inspect.currentframe()).function}) требует доработки")


string_to_int(5)


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            file.name
    except FileNotFoundError:
        print("Файл не найден")
    else:
        print("Такой файл есть")
    finally:
        try:
            file.close()
        except UnboundLocalError:
            print(f'Файл {filename} не открывался')



def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    if any(not isinstance(x, (int, float)) for x in (a, b)):
        raise TypeError("Неверный тип аргументов")
    try:
        return a / b
    except:
        print("Деление на ноль не возможно")
        raise ZeroDivisionError("Делитель равен нулю")


assert divide_numbers(2, 1) == 2
assert divide_numbers(100, 50) == 2
assert divide_numbers(1, 2) == 0.5
assert divide_numbers(100, 100) == 1
assert divide_numbers(-22, 2) == -11


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except (IndexError, TypeError):
        print("Неверные значения или индекса или типа данных")