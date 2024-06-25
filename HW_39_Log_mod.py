"""
Модуль логирования

"""

import logging

log_38I = logging.getLogger('HW_38I')
log_38I.setLevel(logging.INFO)
fh_38I = logging.FileHandler('HW_38I.log','w','utf-8')
formatter = logging.Formatter('%(asctime)s ===== %(name)s ===== %(levelname)s ====== %(message)s')
fh_38I.setFormatter(formatter)
log_38I.addHandler(fh_38I)

log_38D = logging.getLogger('HW_38D')
log_38D.setLevel(logging.DEBUG)
fh_38D = logging.FileHandler('HW_38D.log','w','utf-8')
formatter = logging.Formatter('%(asctime)s ===== %(name)s ===== %(levelname)s ====== %(message)s')
fh_38D.setFormatter(formatter)
log_38D.addHandler(fh_38D)

log_fruit = logging.getLogger('Fruits_tast')
log_fruit.setLevel(logging.INFO)
fh_fruit = logging.FileHandler(filename='fruits.log', mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s ===== %(name)s ===== %(levelname)s ====== %(message)s')
fh_fruit.setFormatter(formatter)
log_fruit.addHandler(fh_fruit)