cars_count = 0
All_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in range(len(All_cars)):
    print('Я езжу на автомабиле марки\t',
          All_cars[i],
          '\tЗначение переменной cars_count на этом шаге:\t',
          cars_count)
    cars_count += 10