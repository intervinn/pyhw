import datetime
from item import Item

class Car(Item):
    
    def __init__(self, name: str, date_created: datetime.datetime, manufacturer: str, engine_capacity: int, color: int, price: int) -> None:
        super().__init__(name, date_created)
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, new: str) -> None:
        self.__manufacturer = new
    
    @property
    def engine_capacity(self) -> int:
        return self.__engine_capacity
    @engine_capacity.setter
    def engine_capacity(self, new: int) -> None:
        self.__engine_capacity = new
    
    @property
    def color(self) -> int:
        return self.__color
    @color.setter
    def color(self, new: int) -> None:
        self.__color = new
    
    @property
    def price(self) -> int:
        return self.__price
    @price.setter
    def price(self, new) -> None:
        self.__price = new
