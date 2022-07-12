from dir3_4_add_sub_mul_truediv.CODE_3_4_6 import *

if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        stack.push_back(StackObj(str(i)))

    for i in range(2):
        obj = stack.pop_back()

    # добавление нового объекта класса StackObj в конец односвязного списка st
    stack = stack + StackObj('11')
    stack += StackObj('12')

    # добавление нескольких объектов в конец односвязного списка
    stack = stack * ['data_1', 'data_2', ..., 'data_N']
    stack *= ['data_1', 'data_2', ..., 'data_N']
    print(stack)

