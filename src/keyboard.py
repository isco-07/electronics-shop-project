from src.item import Item
from src.mixin import MixinLog


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)
