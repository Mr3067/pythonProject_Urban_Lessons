"""
Введение в логирование https://www.youtube.com/watch?v=_HGfpa7Km5E
Логирование в несколько мест назначения https://www.youtube.com/watch?v=yJFCwbnpVcs
Конфигурирование логирования https://www.youtube.com/watch?v=u2K_ygUrAEo

"""

import logging
import HW_38
import Fruits_test



def summm(n):
    for i in range(n):
        logging.debug(f'i = {i},')
        a = i * 2
        logging.warning(f'a = {a},')
        b = i * 3
        logging.debug(f'b = {b},')
        c = a + b
        logging.debug(f'c = {c},')
    return c


# logging.basicConfig(level=logging.DEBUG)#, filename='logg1.log')
# for pp in range(1, 11):
#     logging.info(f'pp = {pp}, summm(pp) = {summm(pp)}')
#     try:
#         logging.info("Программа работает")
#         summm(pp)/(summm(pp)-45)
#         logging.info("========================================")
#     except Exception:
#         logging.info("Вызвана ошибка ******************************")
#         logging.exception(f'При pp = {pp}, summm(pp) = {summm(pp)}')

alex = HW_38.Student('Alex')
alex.run()
alex.walk()
alex.run()
Fruits_test.market_prices('Danilov ')

