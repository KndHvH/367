

class Wien():

    def __init__(self) -> None:

        self.__temp = self.__get_temp()
        self.__temp_type = self.__get_temp_type()
        self.__comp = self.__get_comp()
        self.__comp_type = self.__get_comp_type()
        self.__b_constant = 2.898*(10**-3)

    def __get_temp(self):
        while True:
            try:
                temp = input('temperatura ')
                if temp != '':
                    temp = float(temp)
                return temp
            except:
                pass

    def __get_temp_type(self):
        while True:
            try:
                type = input('(k)kelvin (c)celcius ')
                if type != 'k' and type != 'c':
                    raise Exception
                return type

            except:
                pass

    def __get_comp(self):
        while True:
            try:
                comp = input('comprimento ')
                if comp != '':
                    comp = float(comp)
                return comp
            except:
                pass

    def __get_comp_type(self):
        while True:
            try:
                type = input('(m)metro (a)A ')
                if type != 'm' and type != 'a':
                    raise Exception
                return type

            except:
                pass

    def calculate(self):
        if not ((self.__comp == '' and self.__temp == '') or (self.__comp != '' and self.__temp != '')):
            if self.__comp == '':
                result = self.calculate_comp()
            if self.__temp == '':
                result = self.calculate_temp()

            return result

        print('ONE atribute must be empty')

    def calculate_comp(self):
        if self.__temp_type == 'c':
            self.__temp = self.__c_to_k(self.__temp)

        print(self.__temp)
        calculated_comp = self.__b_constant / self.__temp

        if self.__comp_type == 'a':
            calculated_comp = self.__m_to_a(calculated_comp)

        return calculated_comp

    def calculate_temp(self):
        if self.__comp_type == 'a':
            self.__comp = self.__a_to_m(self.__comp)

        calculated_temp = self.__b_constant / self.__comp

        if self.__temp_type == 'c':
            calculated_temp = self.__k_to_c(calculated_temp)
        return calculated_temp

    def __c_to_k(self, c):
        return c+273.15

    def __k_to_c(self, k):
        return k-273.15

    def __a_to_m(self, a):
        return a * (10**-10)

    def __m_to_a(self, m):
        return m / (10**10)


exercice = Wien()

print(exercice.calculate())
