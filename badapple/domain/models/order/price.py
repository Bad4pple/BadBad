class Prices:
    def __init__(self,prices: list) -> None:
        self.__total_price = 0
        self.__prices = prices

    def calculate_total_price(self):
        for index in self.__prices:
            self.__total_price += index.quantities * 30
        return self.__total_price   
        # print(self.__prices )