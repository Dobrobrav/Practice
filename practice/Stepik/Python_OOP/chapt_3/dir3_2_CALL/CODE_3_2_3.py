from typing import Tuple


class ImageFileAcceptor:
    _extensions: Tuple[str, ...]

    def __init__(self, extensions: Tuple[str, ...]):
        self._extensions = extensions

    def __call__(self, file_name: str, *args, **kwargs) -> bool:
        return file_name.split('.')[-1] in self._extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]


if __name__ == '__main__':
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
    acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
    image_filenames = filter(acceptor, filenames)
    print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]