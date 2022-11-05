stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    """ Class that represents a string of words and has a list of these words;
    the class implements operations '<', '>', '<=', '>='.
    """

    lst_words: list[str]

    def __init__(self, lst_words: list[str]):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, StringText):
            return NotImplemented
        return len(self) < len(other)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, StringText):
            return NotImplemented
        return len(self) <= len(other)

    def __repr__(self):
        return str(self.lst_words)


if __name__ == '__main__':
    lst_text = [
        StringText(
            [word.strip("–?!,.;")
             for word in line.replace(' – ', ' ').split()]
        )
        for line in stich
    ]

    lst_text_sorted = sorted(lst_text, reverse=True)

    lst_text_sorted = [' '.join(word for word in string_text.lst_words)
                       for string_text in lst_text_sorted]
