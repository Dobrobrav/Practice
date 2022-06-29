from enum import Enum
from typing import List


class Direction(Enum):
    left = 1
    right = 0


class TreeObj:
    """ Node for decision tree """

    _question: str
    _left: 'TreeObj' = None
    _right: 'TreeObj' = None

    def __init__(self, question):
        self.question = question


class DecisionTree:
    """ Tree with nodes containing questions and results """

    root: TreeObj
    # enum_to_

    @classmethod
    def predict(cls, root: TreeObj, x: List[str]):
        pass

    @classmethod
    def add_obj(cls, obj: 'DecisionTree', node: object):
        pass