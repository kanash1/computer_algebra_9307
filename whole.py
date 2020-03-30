class Whole:
    def __init__(self, number):
        self.sign = 0

        if number[0] == "-":
            self.number = [int(sym) for sym in number[1:]]
            self.sign = 1
        else:
            self.number = [int(sym) for sym in number]
            
        self.size = len(number)

    # сложение целых
    def __add__(self, another):
        pass

    # вычитание целых
    def __sub__(self, another):
        pass

    # умножение натуральных
    def __mul__(self, another):
        pass

    # абсолютная величина
    def ABS_Z_N(self):
        return self.number

    # определение положительности числа
    def POZ_Z_D(self):
        if self.number[0] == 0:
            number_positivity = 0
        elif self.sign == 1:
            number_positivity = 1
        elif self.sign == 0:
            number_positivity = 2
        return number_positivity
