from typing import Tuple

CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:
    def __new__(cls, title: str, path: str, exts: Tuple[str]):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        return cls.create_linux_filedialog(title, path, exts)

    @staticmethod
    def create_windows_filedialog(title: str, path: str, exts: Tuple[str]):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title: str, path: str, exts: Tuple[str]):
        return LinuxFileDialog(title, path, exts)
