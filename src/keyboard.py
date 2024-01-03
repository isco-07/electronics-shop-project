from src.item import Item
from src.mixin import MixinLog


class Keyboard(Item, MixinLog):
    def change_lang(self):
        MixinLog.change_lang(self)
