from CODE_3_3_4 import *


if __name__ == '__main__':
    words = WordString()
    words.string = "Курс по Python ООП"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")

