def main():
    lst_in = input().split()

    sum_of_lst = sum(
        int(string) for string in lst_in if str_consists_of_int(string)
    )

    print(sum_of_lst)


def str_consists_of_int(string: str):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
