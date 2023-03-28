## CP1 CQUANT


##### Q1
a catastrofe, é um problema que surgiu da tentativa de descrever a radiacao obtida por um objeto quente, primeiramente, concluiram que a intensidade da radiacao era proporcional a temperatura do objeto.
porem quando tentaram medir a intensidade de um corpo negro na faixa ultravioleta, perceberam que a intensidade aumentava indefinidamente a medida que o comprimento de onda se aproximava de zero.
e a fisica classica nao era capaz de explicar esse comportamento, e essa contradicao ficou conhecida como catastrofe ultravioleta

##### Q2
###### R: 2.89e-6 m

    # Temperatura: 1000
    # (k)Kelvin (c)Celcius: k
    # Comprimento: 
    # (m)Metro (a)A: m
    # Resultado: 2.8980000000000005e-06 m

    class Wien():

        def __init__(self) -> None:

            self.__temp = self.__get_temp()
            self.__temp_type = self.__get_temp_type()
            self.__comp = self.__get_comp()
            self.__comp_type = self.__get_comp_type()
            self.__b_constant = 2.898*(10**-3)
            self.__result = self.calculate()

        def __str__(self) -> str:

            result_value = self.__result[0]
            result_icon = self.__get_icon(self.__result[1])

            message = f'Resultado: {result_value:.2f} {result_icon}'
    
            if result_value < 1:
                message = f'Resultado: {result_value} {result_icon}'

            return message
        

        def __get_icon(self, result_type):

            icon = self.__temp_type
            if result_type == 'c':
                icon = self.__comp_type

            pool = {
                'a': 'Å',
                'm': 'm',
                'k': 'K',
                'c': '°C'
            }

            return pool.get(icon)

        def __get_temp(self):
            while True:
                try:
                    temp = input('Temperatura: ')
                    if temp != '':
                        temp = float(temp)
                    return temp
                except:
                    pass

        def __get_temp_type(self):
            while True:
                try:
                    type = input('(k)Kelvin (c)Celcius: ')
                    if type != 'k' and type != 'c':
                        raise Exception
                    return type

                except:
                    pass

        def __get_comp(self):
            while True:
                try:
                    comp = input('Comprimento: ')
                    if comp != '':
                        comp = float(comp)
                    return comp
                except:
                    pass

        def __get_comp_type(self):
            while True:
                try:
                    type = input('(m)Metro (a)A: ')
                    if type != 'm' and type != 'a':
                        raise Exception
                    return type

                except:
                    pass

        def calculate(self):
            if not ((self.__comp == '' and self.__temp == '') or (self.__comp != '' and self.__temp != '')):
                if self.__comp == '':
                    result = [self.calculate_comp(), 'c']

                if self.__temp == '':
                    result = [self.calculate_temp(), 't']

                return result

            print('ONE atribute must be empty')

        def calculate_comp(self):
            if self.__temp_type == 'c':
                self.__temp = self.__c_to_k(self.__temp)

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
            return m / (10**-10)


    exercice = Wien()

    print(exercice)



##### Q3
###### R: 1.27575e9 J
    stefBoltz = 5.67e-8

    A = 10
    T = 500
    t = 3600
    E = stefBoltz * T**4 * A * t

    print("A energia total emitida pelo corpo negro é de", E, "Joules.")
    # A energia total emitida pelo corpo negro é de 127575000.0 Joules.

##### Q4
###### R: 4.51e-5 m2

    stefBoltz = 5.67e-8
    T = 2500
    P = 100
    A = P / (stefBoltz * T**4)

    print("A área da superfície é de", A, "metros quadrados.")
    # A área da superfície é de 4.5149911816578484e-05 metros quadrados.

##### Q5
###### R: 6\*10^-3 mK

10μm = 10 * 10^-6
10e-6 * 600k = 0.006mK


##### Q6
plank pensou em agrupar em pacotes a energia emitida baseados em uma constante que desenvolveu, depois einstein explicou que se tratava de um foton 

