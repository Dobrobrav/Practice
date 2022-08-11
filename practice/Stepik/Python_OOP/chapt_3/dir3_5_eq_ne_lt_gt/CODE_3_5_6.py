from string import punctuation
import re


def del_punctuation(string: str) -> str:
    return re.sub(f"[{punctuation}]", '', string)


class Morph:
    """ Class that represents a collection of forms belonging to one word.

    The class implements methods for:
     - adding new forms of the word
     - getting the tuple of the forms
     - comparing the class instance with other words (of str type)
    """

    _forms: list[str]

    def __init__(self, *args: str):
        self._forms = list(args)

    def __repr__(self):
        return str(self._forms[0])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, str):
            return NotImplemented
        return other.lower() in self._forms

    def add_word(self, word: str):
        self._forms.append(word)

    def get_words(self) -> tuple[str, ...]:
        return tuple(self._forms)


if __name__ == '__main__':
    tuples_of_words_to_add = (
        ("связь", "связи", "связью", "связей", "связями", "связях"),
        ("формула", "формулы", "формуле", "формулу", "формулой",
         "формул", "формулам", "формулами", "формулах"),
        ("вектор", "вектора", "вектору", "вектором", "векторе", "векторы",
         "векторов", "векторам", "векторами", "векторах"),
        ("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты",
         "эффектов", "эффектам", "эффектами", "эффектах"),
        ("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях"),
    )
    dict_words = [Morph(*words) for words in tuples_of_words_to_add]

    text = input()

    words = del_punctuation(text).split()

    morphs_occurred_in_text = []
    for word in words:
        if (any(word == morph for morph in dict_words)
                and word not in morphs_occurred_in_text):
            morphs_occurred_in_text.append(word)

    print(len(morphs_occurred_in_text))
