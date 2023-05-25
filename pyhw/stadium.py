import datetime
from item import Item

class Stadium(Item):
    def __init__(self, name: str, date_created: datetime.datetime, country: str, city: str, capacity: int) -> None:
        super().__init__(name, date_created)
        self.__country = country
        self.__city = city
        self.__capacity = capacity
    
    @property
    def country(self) -> str:
        return self.__country
    @country.setter
    def country(self, new: str) -> None:
        self.__country = new
    
    @property
    def city(self) -> str:
        return self.__city
    @city.setter
    def city(self, new: str) -> None:
        self.__city = new

    @property
    def capacity(self) -> int:
        return self.__capacity
    @capacity.setter
    def capacity(self, new: int) -> None:
        self.__capacity = new