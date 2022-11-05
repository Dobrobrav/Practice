def main():
    lst_in = input().split()

    lst_out = [format_str(e) for e in lst_in]


def format_str(string: str):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return string


if __name__ == '__main__':
    main()
