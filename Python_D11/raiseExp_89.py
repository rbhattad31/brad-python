class Coffee:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            # print("Coffee too Hot")
            raise Exception("Coffee too Hot")
        elif self.__temperature < 65:
            # print("Coffee too Cold")
            raise Exception("Coffee too Cold")
        else:
            print("Coffee ok to Drink")


ui = int(input("Enter Coffee Temperature"))
cup = Coffee(ui)
cup.drink_coffee()
