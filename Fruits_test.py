import HW_39_Log_mod

def market_prices(name, **fruits):
    HW_39_Log_mod.log_fruit.info('Начало исполнение функции')
    print("Hello! Welcome to "+name+" Market!")
    for fruit, price in fruits.items():
        HW_39_Log_mod.log_fruit.info(f'Цикл со значениями {fruit, price}')
        price_list = " {} is NTD {} per piece.".format(fruit,price)
        print (price_list)

fruits={"apple":10,
       "banana":8,
       "pineapple":50,
       "mango":45
       }

market_prices('Danilov ', **fruits) #Use **before arguments



