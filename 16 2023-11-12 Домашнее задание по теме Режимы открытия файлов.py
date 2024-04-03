"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/11/12 00:00|Домашнее задание по теме "Режимы открытия файлов"
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
Распечатайте содержимое текстового файла в консоль
Закройте файл

https://urban-university.ru/members/courses/course999421818026/20231112-0000domasnee-zadanie-po-teme-rezimy-otkrytia-fajlov-542449244638

"""

with open("open_file_service", encoding='utf-8', mode='a+') as f:
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

with open("open_file_service", encoding='utf-8') as my_file:
    print(*my_file)
    # инструкция with автоматически закрывает файд без явной инструкции close



