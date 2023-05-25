import datetime
from item import Item


class Book(Item):
    def __init__(self, name: str, date_created: datetime.datetime, publisher: str, genre: str, author: str, price: int) -> None:
        super().__init__(name, date_created)
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    @property
    def publisher(self) -> str:
        return self.__publisher
    @publisher.setter
    def publisher(self, new: str) -> None:
        self.__publisher = new

    @property
    def genre(self) -> str:
        return self.__genre
    @genre.setter
    def genre(self, new: str) -> None:
        self.__genre = new
    
    @property
    def author(self) -> str:
        return self.__author
    @author.setter
    def author(self, new: str) -> None:
        self.__author = new
    
    @property
    def price(self) -> int:
        return self.__price
    @price.setter
    def price(self, new: int) -> None:
        self.__price = new