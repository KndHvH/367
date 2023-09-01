
class Employee:

    def __init__(self, name) -> None:
        self.name = name

    def hitClock(self):
        print('Funcionario Bateu o ponto!')

    def showTasks(self):
        print('Nenhuma Tarefa!')


class Caelum(Employee):

    def showTasks(self):
        print('Nenhuma Tarefa, Caelumer!')

    def showCourses(self, month=None):
        value = 'Nenhum' if month else 'Varios'
        print(f'Cursos: {value}')


class Alura(Employee):

    def showTasks(self):
        print('Nenhuma Tarefa, Alurer!')

    def showUnsolvedQuestions(self):
        print('Mostrando Perguntas sem resposta!')

#mixin
class GoodMorning:
    def __str__(self) -> str:
        return f'Bom Dia! {self.name}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, GoodMorning):
    pass
