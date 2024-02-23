def print_params(param1, param2):
    for i in range(param1):
        print('Повторяемый текст:', param2, '\t Повтор вывода №', i + 1)


def number_iter_prog(case_of_text):
    _iter_prog = False
    while not _iter_prog:
        match case_of_text:
            case 1:
                info_str = '\nКоличество повторов программы:'
            case 2:
                info_str = '\nКоличество повторов вывода текста:'

        _iter_prog = input(info_str)

        if not _iter_prog.isdigit():
            _iter_prog = False
        else:
            _iter_prog = int(_iter_prog)
    return _iter_prog


for _ in range(number_iter_prog(1)):
    iter_number = number_iter_prog(2)
    number2 = False
    while not number2:
        number2 = input('\nВведите выводимый текст:')
        if not number2.isalpha():
            number2 = False

    print_params(iter_number, number2)

print('\n\n The end')
