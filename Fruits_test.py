def market_prices(name, **fruits):
    print("Hello! Welcome to "+name+" Market!")
    for fruit, price in fruits.items():
        price_list = " {} is NTD {} per piece.".format(fruit,price)
        print (price_list)

fruits={"apple":10,
       "banana":8,
       "pineapple":50,
       "mango":45
       }

market_prices('Danilov ', **fruits) #Use **before arguments



