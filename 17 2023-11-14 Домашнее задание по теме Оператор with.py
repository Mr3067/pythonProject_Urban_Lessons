"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/14 00:00|Домашнее задание по теме "Оператор "with".
Создайте новый проект или продолжите работу в текущем проекте

Ваша задача:
Создайте в директории проекта текстовый файл с раширением txt
Добавьте в этот файл следующий текст
# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.

Создайте переменную с этим файлом
Распечатайте содержимое текстового файла в консоль, используя оператор with
Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
Получившийся код прикрепите к заданию текстом
"""

with open("open_file_service2", encoding='utf-8', mode='a+') as f:
    f.write("""# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.""")
    # инструкция with автоматически закрывает файд без явной инструкции close

with open("open_file_service2", encoding='utf-8') as my_file:
    print(*my_file)

"""Менеджер контекста – специальная конструкция управления обращениями к внешним ресурсам.
 Инициируется конструкцией with автоматически закрывает файл без явной инструкции close"""