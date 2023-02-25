from practice.Stepik.Python_OOP.c3_magic_methods.d9_iter_next \
    .code_10 import *

if __name__ == '__main__':
    # took these tests from one student from the OOP-course
    # seem to be fine :)
    list2D = [[1, 2], [3, 4], [5, 6, 7]]
    try:
        st = Matrix(list2D)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

    list2D = [[1, []], [3, 4], [5, 6]]
    try:
        st = Matrix(list2D)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

    try:
        st = Matrix('1', 2, 0)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

    list2D = [[1, 2], [3, 4], [5, 6]]
    matrix = Matrix(list2D)
    assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

    matrix = Matrix(4, 5, 10)
    assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

    try:
        v = matrix[3, -1]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    try:
        v = matrix['0', 4]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    matrix[0, 0] = 7
    assert matrix[0, 0] == 7, "неверно отработал __setitem__"

    try:
        matrix[0, 0] = 'a'
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError в __setitem__"

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 1], [1, 1], [1, 1]])

    try:
        matrix = m1 + m2
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 1], [1, 1]])
    matrix = m1 + m2
    assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
    assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
    assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
           and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

    m1 = Matrix(2, 2, 1)
    id_m1_old = id(m1)
    m2 = Matrix(2, 2, 1)
    m1 = m1 + m2
    id_m1_new = id(m1)
    assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

    matrix = Matrix(2, 2, 0)
    m = matrix + 10
    assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
    assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

    m1 = Matrix(2, 2, 1)
    m2 = Matrix([[0, 1], [1, 0]])
    identity_matrix = m1 - m2  # должна получиться единичная матрица
    assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
           and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
    assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

    matrix = Matrix(2, 2, 1)
    m = matrix - 1
    assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
    assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"

    print('test_3_9_10 - SUCCESS!!')