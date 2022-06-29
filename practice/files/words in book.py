import string
from collections import Counter

with open("book.txt", "r") as book:
    lines = [line for line in book.readlines() if line != "\n"]

    words = (
        word for line in lines
             for word in str(line.translate(str.maketrans('', '', string.punctuation))).replace("—", "").split()
    )

    words_rating = Counter(words)

    print(words_rating)

