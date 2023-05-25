import datetime

class Item:
    def __init__(self, name: str, date_created: datetime.datetime) -> None:
        self.__name = name
        self.__date_created = date_created
    
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, new: str):
        self.__name = new

    @property
    def date_created(self):
        return self.__date_created
    @date_created.setter
    def date_created(self, new: datetime.datetime):
        self.__date_created = new
    
    def print_data(self):
        for _, (k,v) in enumerate(self.__dict__.items()):
            print(k.split("__")[1] + ":", v)