import HW_39_Log_mod

class Student:
    def __init__(self, name):
        self.name = name
        HW_39_Log_mod.log_38I.info(f'New st {self.name}')
        HW_39_Log_mod.log_38D.info(f'New st {self.name}')
        self.distance = 0

    def run(self):
        self.distance += 10
        HW_39_Log_mod.log_38I.info(f'Student {self.name} run;distance {self.distance}')

    def walk(self):
        self.distance += 5
        HW_39_Log_mod.log_38D.info(f'Student {self.name} walk ;distance {self.distance}')

    def __str__(self):
        return self.name