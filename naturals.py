class Natural:
    def __init__(self, num):
        self.num = [int(i) for i in num]
        self.pos = len(self.num) - 1

    def __str__(self):
        return ''.join(map(str, self.num))

    # N-1
    def __cmp__(self, oth):
        if self.pos > oth.pos:
            return 2
        elif self.pos < oth.pos:
            return 1
        else:
            for i in range(self.pos + 1):
                if self.num[i] > oth.num[i]:
                    return 2
                elif self.num[i] < oth.num[i]:
                    return 1
            return 0

    # NZER_N_B
    def isnZero(self):
        if self.pos == 0 and self.num[0] == 0:
            return "нет"
        else:
            return "да"

    # ADD_1N_N
    def addOne(self):
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        i = 0
        while self.num[i] + 1 > 9:
            if i + 1 > self.pos:
                self.num.append(0)
                self.pos += 1
            self.num[i] = 0
            i += 1
        self.num[i] += 1
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить

    # ADD_NN_N
    def sum(self, other):
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        other.num = other.num[::-1]  # если последвательность цифр уже перевернута, то удалить

        if self.pos < other.pos:
            for i in range(other.pos - self.pos):
                self.num.append(0)
            self.pos = other.pos
        temp = 0

        for i in range(other.pos + 1):
            self.num[i] = self.num[i] + other.num[i] + temp
            if self.num[i] > 9:
                temp = 1
            else:
                temp = 0
            self.num[i] = self.num[i] % 10

        if self.pos == other.pos and temp == 1:
            self.num.append(0)
            self.pos += 1

        if self.pos > other.pos and temp == 1:
            j = other.pos + 1
            while self.num[j] + 1 > 9:
                if j + 1 > self.pos:
                    self.num.append(0)
                    self.pos += 1
                self.num[j] = 0
                j += 1
            self.num[j] += 1

        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        other.num = other.num[::-1]  # если последвательность цифр уже перевернута, то удалить

    # N-5 сделал, т.к. похожа на N-10
    # временное решение нужно переделать
    def __sub__(self, oth):
        if self.__cmp__(oth) == 1:
            return -1
        elif self.__cmp__(oth) == 0:
            return Natural('0')
        else:
            res = Natural(self.num)
            for i in range(oth.pos, -1, -1):
                if res.num[i + res.pos - oth.pos] < oth.num[i]:
                    temp = 1
                    res.num[i + res.pos - oth.pos] = 10 + res.num[i + res.pos - oth.pos] - oth.num[i]
                    while res.num[i + res.pos - oth.pos - temp] - 1 < 0 and i - temp < 0:
                        res.num[i + res.pos - oth.pos - temp] = 9
                        temp -= 1
                    res.num[i + res.pos - oth.pos - temp] -= 1
                    if res.num[0] == 0:
                        del res.num[0]
                        res.pos -= 1
                else:
                    res.num[i + res.pos - oth.pos] -= oth.num[i]
            if res.num[0] == 0:
                del res.num[0]
                res.pos -= 1
            return res

    # N-6 временное решение нужно переделать
    def MUL_ND_N(self, numeric):
        return Natural(str(int(str(self)) * numeric))

    # N-7 временное решение нужно переделать
    def MUL_Nk_N(self, numeric):
        return str(self) + '0' * numeric

    # N-8
    def __mul__(self, oth):
        pass

    # N-9
    def SUB_NDN_N(self, oth, numeric):
        if self.__cmp__(oth.MUL_ND_N(numeric)) == 1:
            return -1
        elif self.__cmp__(oth.MUL_ND_N(numeric)) == 0:
            return Natural('0')
        else:
            return self.__sub__(oth.MUL_ND_N(numeric))

    # N-10
    def DIV_NN_Dk(self, oth):
        if self.__cmp__(oth) != 1:
            temp_1 = Natural(''.join(map(str, self.num))[:oth.pos + 1])
            temp_2 = 0
            if temp_1.__cmp__(oth) == 1:
                temp_1.num.append(self.num[oth.pos + 1])
                temp_1.pos += 1
            while temp_1.__cmp__(oth) != 1:
                for i in range(oth.pos, -1, -1):
                    if temp_1.num[i + temp_1.pos - oth.pos] < oth.num[i]:
                        temp_1.num[i + temp_1.pos - oth.pos] = 10 + temp_1.num[i + temp_1.pos - oth.pos] - oth.num[i]
                        temp_1.num[i + temp_1.pos - oth.pos - 1] -= 1
                    else:
                        temp_1.num[i + temp_1.pos - oth.pos] -= oth.num[i]
                if temp_1.num[0] == 0:
                    del temp_1.num[0]
                    temp_1.pos -= 1
                temp_2 += 1
            res = Natural(str(temp_2))
            return int(res.MUL_Nk_N(self.pos - oth.pos - (self.num[0] < oth.num[0])))
        else:
            return -1

    # N-11
    def DIV_NN_N(self, oth):
        if self.__cmp__(oth) != 1:
            temp_1 = Natural(self.num)
            res = 0
            while temp_1.__cmp__(oth) != 1:
                temp_2 = temp_1.DIV_NN_Dk(oth)
                res += temp_2
                temp_1 = temp_1.SUB_NDN_N(oth, temp_2)
            return Natural(str(res))
        else:
            return -1

    # N-12
    def MOD_NN_N(self, oth):
        if self.__cmp__(oth) != 1:
            res = Natural(self.num)
            while res.__cmp__(oth) != 1:
                temp_2 = res.DIV_NN_Dk(oth)
                res = res.SUB_NDN_N(oth, temp_2)
            return res
        else:
            return -1
