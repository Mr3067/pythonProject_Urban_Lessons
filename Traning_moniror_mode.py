"""
Функция получения режимов работы мотнитора.
Результат работы - список из кортежей; в каждом кортеже режим работы монитора

"""


def monitorWH():
    import screeninfo as scr_info

    def clear_chr(input_sting):
        """
        :param input_sting: получает строку буквы и цифры
        :param __doc__:
        :return: выделенные из строки цифры, преобразованные в число на входе строка "width=3840", на выходе цулое 3840
        """
        aa = str()
        for ii in range(len(input_sting)):
            if input_sting[ii].isdigit():
                aa = aa + input_sting[ii]
        return int(aa)

    separ = str(list(scr_info.get_monitors())[0]).split()  # получает значения параметров монитора, разделяет по пробелу
    sc_info_width = []
    sc_info_height = []
    j = z = 0
    for i in range(len(separ)):# находит значения разрешений всех режимов
        if 'width' in separ[i]:
            sc_info_width.extend([j])
            sc_info_width[j] = separ[i]
            j += 1
        elif 'height' in separ[i]:
            sc_info_height.extend([z])
            sc_info_height[z] = separ[i]
            z += 1
    for i in range(len(sc_info_width)):
        sc_info_width[i] = clear_chr(sc_info_width[i])

    for i in range(len(sc_info_height)):
        sc_info_height[i] = clear_chr(sc_info_height[i])

    return list(zip(sc_info_width, sc_info_height))


yy = monitorWH()
print(yy)
