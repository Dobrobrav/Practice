class VideoRating:
    __rating = 0
    MAX_RATING = 5
    MIN_RATING = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self._validate_rating(rating)
        self.__rating = rating

    def _validate_rating(self, rating: int):
        if not (type(rating) is int
                and self.MIN_RATING <= rating <= self.MAX_RATING):
            raise ValueError('неверное присваиваемое значение')


class VideoItem:
    title: str
    descr: str
    path: str
    rating = VideoRating()

    def __init__(self, title: str, descr: str, path: str):
        self.title = title
        self.descr = descr
        self.path = path


if __name__ == '__main__':
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР',
                  'D:/videos/python_oop.mp4')
