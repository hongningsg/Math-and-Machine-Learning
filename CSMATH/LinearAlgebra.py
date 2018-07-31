__all__ = ["Matrix"]

class Matrix():
    def __init__(self, *mat):
        self.__row = 0
        self.__col = 0
        if len(mat) == 0:
            self.__data = []
        elif len(mat) == 2 and type(mat[0]) == int and type(mat[1]) == int:
            self.__data = self.__New(mat[0], mat[1])
            self.__row = mat[0]
            self.__col = mat[1]
        else:
            mat = mat[0]
            assert type(mat) == list, "Input should be list or two integers indicates dimension of matrix."
            if len(mat) == 0:
                self.__init__()
            else:
                self.__data = []
                self.__inner_count(mat)

    def __inner_count(self, submat, depth = 1):
        if type(submat[0]) == list:
            for sub in submat:
                    self.__inner_count(sub, depth + 1)
        else:
            self.__row += 1
            if self.__col != 0:
                assert self.__col == len(submat),"Every row should have the same number of columns."
            else:
                self.__col = len(submat)
            if depth == 1:
                self.__data = submat
            else:
                self.__data.append(submat)

    def get_col(self):
        return self.__col

    def get_row(self):
        return  self.__row

    def Shape(self):
        return self.__row, self.__col

    def Peek_shape(self):
        return str(self.__row) + " x " + str(self.__col)

    def __New(self, n, m):
        re = []
        assert n >= 0 and m >= 0, "Input dimensions should be natural numbers."
        if n <= 1 or m == 0:
            return [0]*m
        for _ in range(n):
            re.append([0]*m)
        return re

    def __str__(self):
        if self.__row == 0 or self.__col == 0:
            return "[]"
        return self.__matprint(self.__data)

    def __matprint(self, sublist, printr = "", depth = 1):
        printr += "["
        if type(sublist[0]) == list:
            for i in range(len(sublist)):
                printr = self.__matprint(sublist[i], printr, depth + 1)
                if depth == 1 and i != len(sublist) - 1:
                    printr += "\n"
        else:
            for i in range(len(sublist)):
                printr += str(sublist[i])
                if i != len(sublist) - 1:
                    printr += " "
        printr += "]"
        return printr

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if type(other) is Matrix:
            assert other.Shape() == self.Shape(), "Two matrices should have the same shape."
            return Matrix(self.__matadd(self.__data, other))
        else:
            return Matrix(self.__mataddi(self.__data, other))
        # if type(self.__data[0]) == int:
        #     return self.__vector_add(other)
        # else:
        #     return self.__matrix_add(other)

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __radd__(self, other):
        return self.__add__(other)

    def __mataddi(self, mat, other):
        if type(mat[0]) == list:
            for m in mat:
                self.__mataddi(m, other)
        else:
            for i in range(len(mat)):
                mat[i] += other
        return mat

    def __matadd(self, mat, other):
        if type(mat[0]) == list and type(other[0]) == list:
            re = []
            for i in range(len(mat)):
                tmp_col = []
                for j in range(len(mat[0])):
                    tmp_col.append(mat[i][j] + other[i][j])
                re.append(tmp_col)
            return re
        elif type(mat[0]) == list:
            return self.__matadd(mat, [other])
        elif type(other[0]) == list:
            return self.__matadd([mat], other)
        else:
            re = []
            for i in range(len(mat)):
                re.append(mat[i] + other[i])
            return re
