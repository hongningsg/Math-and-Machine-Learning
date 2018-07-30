__all__ = ["Matrix"]

class Matrix():
    def __init__(self, *mat):
        if len(mat) == 0:
            self.__data = []
            self.__row = 0
            self.__col = 0
        else:
            mat = mat[0]
            if len(mat) == 0:
                self.__init__()
            else:
                self.__data = mat
                if type(mat[0]) == list:
                    l = len(mat[0])
                    for i in range(len(mat)):
                        assert (len(mat[i]) == l),"Every row should have the same number of columns."
                    self.__col = l
                    self.__row = len(mat)
                else:
                    self.__col = len(mat)
                    self.__row = 1

    def get_col(self):
        return self.__col

    def get_row(self):
        return  self.__row

    def Shape(self):
        return self.__row, self.__col

    def Peek_shape(self):
        return str(self.__row) + " x " + str(self.__col)

    def New(self, n, m):
        for _ in range(n):
            self.__data.append([0]*m)
        self.__row = n
        self.__col = m

    def __str__(self):
        if self.__row == 0:
            return "[]"
        if type(self.__data[0]) == int:
            return self.__vector_print()
        return self.__matrix_print()

    def __vector_print(self):
        printr = "["
        for i in range(self.__col):
            printr += str(self.__data[i])
            if i != self.__col - 1:
                printr += " "
        printr += "]"
        return  printr

    def __matrix_print(self):
        printr = ""
        for i in range(self.__row):
            printr += "["
            for j in range(self.__col):
                printr += str(self.__data[i][j])
                if j != self.__col - 1:
                    printr += " "
            printr += "]\n"
        return printr

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if type(self.__data[0]) == int:
            return self.__vector_add(other)
        else:
            return self.__matrix_add(other)

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __radd__(self, other):
        return self.__add__(other)

    def __vector_add(self, other):
        re = []
        if type(other) == int:
            for i in range(self.__col):
                re.append(self.__data[i] + other)
        else:
            assert type(other) is Matrix, "The other component need to be Matrix."
            assert other.Shape() == self.Shape(), "Two matrices should have the same shape."
            for i in range(self.__col):
                re.append(self.__data[i] + other[i])
        return Matrix(re)

    def __matrix_add(self, other):
        re = []
        if type(other) == int:
            for i in range(self.__row):
                tmp_col = []
                for j in range(self.__col):
                    tmp_col.append(self.__data[i][j] + other)
                re.append(tmp_col)
        else:
            assert type(other) is Matrix, "The other component need to be Matrix."
            assert other.Shape() == self.Shape(), "Two matrices should have the same shape."
            for i in range(self.__row):
                tmp_col = []
                for j in range(self.__col):
                    tmp_col.append(self.__data[i][j] + other[i][j])
                re.append(tmp_col)
        return Matrix(re)