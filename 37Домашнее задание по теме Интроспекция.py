"""
2023/12/31 00:00|Домашнее задание по теме "Интроспекция"

https://urban-university.ru/members/courses/course999421818026/20231231-0000domasnee-zadanie-po-teme-introspekcia-748607565945

"""
import inspect
import math
import requests
import sys
from collections import defaultdict
from pprint import pprint

def introspection_info(obj=math):
    under_line = defaultdict(list)
    for attr in dir(obj):
        get_attr = getattr(obj, attr)
        if inspect.isbuiltin(get_attr):
            under_line['builtin_function_or_method'].append(attr)
        if inspect.isfunction(get_attr):
            under_line['functions'].append(attr)
        if inspect.ismethod(get_attr):
            under_line['methods'].append(attr)
        if inspect.isclass(get_attr):
            under_line['class'].append(attr)
        if inspect.ismodule(get_attr):
            under_line['modules'].append(attr)
        if attr.startswith('_'):
            under_line['privet attributes'].append(attr)
        if callable(get_attr):
            under_line['callable'].append(attr)
    under_line['module'].append(sys.modules[__name__])

    return under_line

number_info = introspection_info(42)
pprint(number_info)

