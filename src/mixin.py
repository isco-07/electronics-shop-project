class MixinLog:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language


