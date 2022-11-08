
class Program:

    info = 'Father class'

    def __init__(self, name, year, likes=0) -> None:

        self.__name = name
        self.__year = year
        self.__likes = likes

    def liked(self):
        self.__likes += 1

    def __str__(self):
        likes = f'Likes: {self.likes}' if self.likes > 1 else f'Like: {self.likes}'
        return f'Name: {self.name} \nYear: {self.year}\n{likes}'

    @property
    def name(self):
        return self.__name.title()

    @property
    def year(self):
        return self.__year

    @property
    def likes(self):
        return self.__likes

    @classmethod
    def info(cls):
        return cls.info


class Film(Program):

    def __init__(self, name, year, duration, likes=0) -> None:
        super().__init__(name, year, likes)

        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        likes = f'Likes: {self.likes}' if self.likes > 1 else f'Like: {self.likes}'
        return f'Name: {self.name} \nYear: {self.year}\nDuration: {self.duration} min\n{likes}'


class Serie(Program):

    def __init__(self, name, year, seasons, likes=0) -> None:
        super().__init__(name, year, likes)

        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons

    def __str__(self):
        likes = f'Likes: {self.likes}' if self.likes > 1 else f'Like: {self.likes}'
        seasons = f'{self.seasons} Seasons' if self.seasons > 1 else f'{self.seasons} Season'
        return f'Name: {self.name} \nYear: {self.year}\nDuration: {seasons}\n{likes}'


class Playlist(list):

    def __init__(self, name, programs) -> None:
        self.__name = name
        self.__programs = programs

    def __getitem__(self, item):
        return self.__programs[item]

    def __str__(self) -> str:
        return f'Name: {self.name}\nSize: {len(self)}'

    def __len__(self):
        return len(self.__programs)

    def showcase(self):
        print(self)
        for i in self:
            print(10*'--')
            print(i)

    @property
    def name(self):
        return self.__name

    @property
    def programs(self):
        return self.__programs


vingadores = Film('Vingadores', 2015, 160)
starwars = Film('star wars', 1999, 130)
got = Serie('Game of Thrones', 2012, 8)
dark = Serie('dark', 2019, 3)
the100 = Serie('The 100', 1900, 1)


dark.liked()
dark.liked()
dark.liked()
dark.liked()
got.liked()
got.liked()
starwars.liked()
starwars.liked()
starwars.liked()
vingadores.liked()


programs = [vingadores, got, starwars, dark, the100]

favoritos = Playlist('Favorites', programs)

favoritos.showcase()
