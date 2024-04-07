# функция Errortry получает неопределенное количество аргументов, но может обработать только два
# при превышении количества аргументов генереруется исключение

class InvalidDataException(ValueError):
    pass
class ProcessingException(ZeroDivisionError):
    pass

IDE = InvalidDataException('Ошибка значений или данных')
PE = ProcessingException('Деление на нУль')
def Errortry(*args):
    if len(args)> 2:
        raise IDE
    else:
        try:
            print( args[0]/args[1])
            return args[0]/args[1]
        except ZeroDivisionError: #обработка исключения с вызовом самописного исключения
            raise PE


def third(*args):
    print('Begin third')
    Errortry(*args)
    print('End third')
def second(*args):
    print('Begin second')
    third(*args)
    print('End second')

def first(*args):
    print('Begin first')
    second(*args)
    print('End first')


assert first(100,2) == 50.0