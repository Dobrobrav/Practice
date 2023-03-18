from string import ascii_lowercase, digits


def main():
    string = "white5 red4 blue1 black3 purple2"
    colors = get_colors_sorted_by_order(string)

    print(colors)


def get_colors_sorted_by_order(string: str) -> list[str]:
    colors_with_order = string.split()
    colors_with_order.sort(key=lambda color_with_order: _get_order(color_with_order))
    res = [_get_color(color_with_order) for color_with_order in colors_with_order]

    return res


def _get_order(string: str) -> int:
    return int(string.lstrip(ascii_lowercase))


def _get_color(string: str) -> str:
    return string.rstrip(digits)


if __name__ == '__main__':
    main()
