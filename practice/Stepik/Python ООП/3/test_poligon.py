from dir3_4_add_sub_mul_truediv.CODE_3_4_8 import *

if __name__ == '__main__':
    my_budget = Budget()
    my_budget.add_item(Item("Курс по Python ООП", 2000))
    my_budget.add_item(Item("Курс по Django", 5000.01))
    my_budget.add_item(Item("Курс по NumPy", 0))
    my_budget.add_item(Item("Курс по C++", 1500.10))

    # вычисление общих расходов
    s = 0
    for x in my_budget.get_items():
        s = s + x

