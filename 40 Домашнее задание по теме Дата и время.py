"""
2024/01/24 00:00|Домашнее задание по теме "Дата и время"
"""

from datetime import datetime


class SuperDate(datetime):
    SEASON_DICT = {
        'Spring': {3, 4, 5},
        'Summer': {6, 7, 8},
        'Autumn': {9, 10, 11},
        'Winter': {12, 1, 2},
    }

    TIME_OF_DAY_DICT = {
        'Night':   {0, 1, 2, 3, 4, 5},
        'Morning': {6, 7, 8, 9, 10, 11},
        'Day':     {12, 13, 14, 15, 16, 17},
        'Evening': {18, 19, 20, 21, 22, 23}
    }

    def __init__(self, *args):
        self.date_time_obj = datetime.strptime(' '.join(str(i) for i in args),
                                                   '%Y %m %d %H')


    def get_season(self):
        for s, m in SuperDate.SEASON_DICT.items():
            if self.date_time_obj.month in m:
                return s

    def get_time_of_day(self):
        for s, m in SuperDate.TIME_OF_DAY_DICT.items():
            if self.date_time_obj.hour in m:
                return s


if __name__ == '__main__':
    try:
        a = SuperDate(2024, 2, 22, 12)
    except ValueError as e:
        print(f'Неверный формат введеных аргументов, значение ошибки: {e}')
    else:
        print(a.get_season())
        print(a.get_time_of_day())


