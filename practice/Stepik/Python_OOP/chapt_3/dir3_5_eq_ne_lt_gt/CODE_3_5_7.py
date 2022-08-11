class FileAcceptor:
    """ Functor for filtering filenames with right extensions.

    Class implements:
     - the '+' operation by combining extensions of both operands
     - the call method that checks if the filename has a correct extension
     """

    _extensions: set[str]

    def __init__(self, *args: str):
        self._extensions = set(args)

    def __call__(self, extension: str) -> bool:
        """ Return true or false depending, on
        weather the filename has a correct extension.
        """
        dot_index = extension.rfind('.')
        return extension[dot_index + 1:] in self._extensions

    def __add__(self, other: object) -> 'FileAcceptor':
        if not isinstance(other, FileAcceptor):
            return NotImplemented
        return FileAcceptor(*(self.extensions | other.extensions))

    @property
    def extensions(self) -> set[str]:
        return self._extensions
