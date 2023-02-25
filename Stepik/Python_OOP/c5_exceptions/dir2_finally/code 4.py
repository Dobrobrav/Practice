def main():
    a, b = input().split()

    res = a + b
    try:
        res = int(a) + int(b)
    except ValueError:
        try:
            res = float(a) + float(b)
        except ValueError:
            pass
    finally:
        print(res)


if __name__ == '__main__':
    main()
