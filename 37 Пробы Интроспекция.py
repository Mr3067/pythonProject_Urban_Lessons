"""
Часть 1 https://www.youtube.com/watch?v=Iifhxk33wj4
Часть 2 https://www.youtube.com/watch?v=Cz6X7-d8Dws
Часть 3 https://www.youtube.com/watch?v=BDHaRomSYNQ

"""
import re

import requests
import inspect
import sys
from pprint import pprint

some_str = 'string obj'
some_num = 42
some_list = [some_str, some_num]


def some_func(param, param_2='n/a'):
    print('my param', param, param_2)


class SomeClass(requests.HTTPError):
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


class SomeClass2(SomeClass):
    pass


some_object = SomeClass()
rq = requests


# print(type(some_str) is str)
# print(type(some_num))
# print(type(some_list))
# print(type(SomeClass))
# print(type(some_object))
# print(type(rq))

# pprint(dir(some_str))
# pprint(dir(some_num))
# pprint(dir(some_list))
# for i in dir(some_list):
#     pprint(eval('some_list'+'.'+i))
# pprint(dir(SomeClass))
# pprint(dir(some_object))

# pprint(dir(rq))
# pprint(dir(some_func))
# pprint(dir(requests))
#
# pprint(hasattr(rq, 'get'))
# pprint((hasattr(some_object,'attribute_2')))
# pprint(getattr(some_object, 'attribute_2', -55))

# pprint(callable(some_str))
# pprint(callable(some_num))
# pprint(callable(some_list))
# for i in dir(rq):
#     print(i, callable(getattr(rq,i)))

# pprint(callable(SomeClass))
# pprint(callable(some_object))
# pprint(callable(some_func))

# respons = requests.get(url='https://google.com')
# for i in dir(respons):
#     print(i, callable(getattr(respons,i)))


# print(issubclass(SomeClass2,requests.HTTPError))

# print(inspect.isbuiltin('+'))
# def f(x, y=1, z=2):
#     pass


# print(inspect.isbuiltin(abs))
# a = inspect.signature(f)
# for i,ii in a.parameters.items():
#     pprint(dir(ii))

# a = inspect.signature(f)
# print(getattr(a.parameters['y'],'name'))
# for j in a.parameters.keys():
#     for i in dir(a.parameters[f'{j}']):
#       if not i.startswith('_') and not str.istitle(i[1]):
#            print(i, '---->', getattr(a.parameters[f'{j}'], f'{i}'))
#            if str(getattr(a.parameters[f'{j}'], f'{i}')) == "class 'inspect._empty":
#                pprint('--------------->',dir(getattr(a.parameters[f'{j}'], f'{i}')))


# pprint(dir(sys))

# for i in dir(sys):
#     if not i.startswith('_') and not str.istitle(i[1]):
#         print(i,'------->', getattr(sys,f'{i}'))

# pprint(dir(__builtins__))

respons = requests.get(url='https://google.com')
pprint(getattr(respons,'connection'))
print(type(respons))
print(isinstance(respons, requests.Response))