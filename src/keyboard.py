from src.item import Item
from src.mixin import MixinLog


class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        else:
            self.__language = 'EN'
            return self.language

