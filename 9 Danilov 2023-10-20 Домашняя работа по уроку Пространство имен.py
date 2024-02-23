""""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/10/20 00:00|Домашняя работа по уроку "Пространство имен."
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию def test_function
Создайте другую функцию внутри функции inner_function, функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
Полученный код напишите в ответ к домашему заданию
Урок "Пространства имен и области видимости"

"""


def test_function():
    _g_Local = 200
    print('Переvенная _g_Local на уровне функции test_function', _g_Local, 'id _g_Local:', id(_g_Local),
          'и Глобальная h:', _h_Global)

    def inner_function():
        # nonlocal _g_Local
        # print('Вызов переменной _g_Local, определенной test_function, до переопределения в nner_function:', _g_Local,
        #       'id _g_Local:', id(_g_Local), 'и Глобальная h:', _h_Global)
        _g_Local = 1000
        print('Вызов переменной _g_Local после переопределения в nner_function:\t', _g_Local, '\t', '\t',
              ' \t id _g_Local:',
              id(_g_Local), '\tи Глобальная h:', _h_Global)
        print('Я в области видимости функции test_function')
        return

    inner_function()
    print('Вызов переменной _g_Local, после выхода из функции nner_function:', _g_Local, 'id _g_Local:', id(_g_Local),
          'и Глобальная h:', _h_Global)

    return


_h_Global = 1500

test_function()
print(_h_Global)
