class Client:

    def __init__(self, name) -> None:
        self.__name = name


    @property
    def name(self):
        return self.__name.title()