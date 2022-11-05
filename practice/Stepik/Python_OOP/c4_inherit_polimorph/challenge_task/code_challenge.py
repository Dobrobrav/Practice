from typing import List, Tuple


class Vertex:
    _links: List['Link']

    def __init__(self):
        self.links = []

    @property
    def links(self) -> List['Link']:
        return self._links.copy()

    @links.setter
    def links(self, links):
        self._links = links


class Link:
    _v1: Vertex
    _v2: Vertex
    _dist: float = 1

    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2

    def __hash__(self):
        return hash((self._v1, self._v2))

    def __eq__(self, other: object):
        if not isinstance(other, Link):
            return NotImplemented
        return hash(self) == hash(other)

    @property
    def v1(self) -> Vertex:
        return self._v1

    @property
    def v2(self) -> Vertex:
        return self._v2

    @property
    def dist(self):
        return

    @dist.setter
    def dist(self, dist: float):
        self._dist = dist


class LinkedGraph:
    _links: List[Link]
    _vertex: List[Vertex]

    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if link not in self._links:
            self._links.append(link)
            self._add_vertexes_from_link(link)

    def _add_vertexes_from_link(self, link: Link):
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

    def find_path(self, start_v: Vertex,
                  stop_v: Vertex) -> Tuple[List[Vertex], List[Link]]:
        """ Return the shortest path from start_v to stop_v. """

    def _get_path_recursive(self, start_v: Vertex,
                            stop_v: Vertex):


class Station(Vertex):
    name: str

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1: Vertex, v2: Vertex, dist: float):
        super().__init__(v1, v2)
        self._dist = dist
