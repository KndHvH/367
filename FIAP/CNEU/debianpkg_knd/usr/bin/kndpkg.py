from math import dist
import csv


class KndEuclides:

    def __init__(self) -> None:
        self.__euclides_list = self.__get_csv()
        self.__biggest_distance = -10000.0
        self.__biggest_distance_coord_pair = ()

    def __str__(self) -> str:

        self.__calculate_from_list()

        distance = self.__biggest_distance
        pair = self.__biggest_distance_coord_pair

        return f'A maior distancia é de {distance:.2f} das coordenadas {pair}'

    def __calculate_from_list(self):
        euclides_list = self.__euclides_list

        for _, value in enumerate(euclides_list):
            x = value[0].split(',')
            y = value[0].split(',')
            distance = self.__calculate_euclides(
                int(x[0]), int(x[1]), int(y[0]), int(y[1]))

            if distance > self.__biggest_distance:
                self.__biggest_distance = distance
                self.__biggest_distance_coord_pair = value

    def __get_csv(self):
        euclides_list = []

        with open('~/csv.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                euclides_list.append((row[1], row[2]))

        return euclides_list[1:]

    def __calculate_euclides(self, x1=0, x2=0, y1=0, y2=0, z1=0, z2=0):

        point1 = (x1, y1, z1)

        point2 = (x2, y2, z2)

        return dist(point1, point2)


euclides = KndEuclides()

print(euclides)
