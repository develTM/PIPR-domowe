class Polynomial():
    def check_input(self, polynomial):
        if not isinstance(polynomial, list):
            raise Exception(TypeError)
        elif polynomial == []:
            raise Exception(ValueError)
        elif False in [len(element) == 2 for element in polynomial]:
            raise Exception(ValueError)
        coefficient_list = []
        for i in polynomial:
            if i[1] == 0:
                raise Exception(ValueError)
            coefficient_list.append(i[0])
        if len(set(coefficient_list)) != len(polynomial):
            raise Exception(ValueError)
        for i in coefficient_list:
            if i < 0:
                raise Exception(ValueError)

    def __init__(self, polynomial):
        self.check_input(polynomial)
        polynomial.sort(key = lambda x: x[0])
        self.polynomial = []
        for element in polynomial:
            self.polynomial.append(element)

    def __str__(self):
        string = ''
        for element in self.polynomial:
            if element[0] == 0:
                string += str(element[1])
            elif element[0] == 1 and element[1] == 1:
                string += 'x'
            elif element[0] == 1:
                string += str(element[1]) + 'x'
            elif element[1] == 1:
                string += 'x^' + str(element[0])
            else: string += str(element[1]) + 'x^' + str(element[0])
            string += '+'
        return string[0:-1]

    def sortandvalidate(self):
        self.polynomial.sort(key=lambda x: x[0])
        while 0 in [i[1] for i in self.polynomial]:
            for element in self.polynomial:
                if element[1] == 0:
                    self.polynomial.remove(element)

    def add(self, other):
        self.check_input(other)
        new_polynomial = []
        coefficients_other = []
        for element in other:
            coefficients_other.append(element[0])
        for element in self.polynomial:
            if element[0] not in coefficients_other:
                new_polynomial.append(element)
            else:
                for other_element in other:
                    if other_element[0] == element[0]:
                        new_polynomial.append((element[0], other_element[1] + element[1]))
                        other.remove(other_element)
        for element in other:
            new_polynomial.append(element)
        self.polynomial = new_polynomial
        self.sortandvalidate()

    def substract(self, other):
        self.check_input(other)
        new_polynomial = []
        coefficients_other = []
        for element in other:
            coefficients_other.append(element[0])
        for element in self.polynomial:
            if element[0] not in coefficients_other:
                new_polynomial.append(element)
            else:
                for other_element in other:
                    if other_element[0] == element[0]:
                        new_polynomial.append((element[0], other_element[1] - element[1]))
                        other.remove(other_element)
        for element in other:
            new_polynomial.append((element[0], -element[1]))
        self.polynomial = new_polynomial
        self.sortandvalidate()

    def coefficient(self, x):
        for element in self.polynomial:
            if element[0] == x:
                return element[1]
        raise Exception(ValueError)

    def degree(self):
        return max([i[0] for i in self.polynomial])

    def value(self, x):
        suma = 0
        for element in self.polynomial:
            suma += element[1] * (x ** element[0])
        return suma

polynomial = Polynomial([(0, 4), (1, 2), (6, 6)])
#print(polynomial.__str__())
polynomial.add([(1, 1), (6, 6), (7, 7), (200, 100), (10, 10)])
polynomial.substract([(0, 4), (1, 3)])

print(polynomial.__str__())

print(polynomial.value(4))

print(polynomial.degree())