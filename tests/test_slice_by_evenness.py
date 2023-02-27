import pytest
from some_programs.slice_by_evenness import slice_by_evenness


@pytest.mark.parametrize('sequence, res', (
        ((), []),
        ([], []),
))
def test_empty_sequence(sequence, res):
    assert slice_by_evenness(sequence) == res


@pytest.mark.parametrize('sequence, res', (
        ((1, 3, 5, 9, 13, 11, 7, 111), [1, 3, 5, 9, 13, 11, 7, 111]),
        ([1, 3, 5, 9, 13, 11, 7, 111], [1, 3, 5, 9, 13, 11, 7, 111]),
))
def test_even_integers_sequence(sequence, res):
    assert slice_by_evenness(sequence) == res


@pytest.mark.parametrize('sequence, res', (
        ((0, 2, 4, 8, 6, 14, 10, 12), [0, 2, 4, 8, 6, 14, 10, 12]),
        ([0, 2, 4, 8, 6, 14, 10, 12], [0, 2, 4, 8, 6, 14, 10, 12]),
))
def test_odd_integers_sequence(sequence, res):
    assert slice_by_evenness(sequence) == res


@pytest.mark.parametrize('sequence, res', (
        ((1, 2, 4, 5, 3, 7, 6, 8), [[1], [2, 4], [5, 3, 7], [6, 8]]),
        ([1, 2, 4, 5, 3, 7, 6, 8], [[1], [2, 4], [5, 3, 7], [6, 8]]),
))
def test_regular_case(sequence, res):
    assert slice_by_evenness(sequence) == res


if __name__ == '__main__':
    pytest.run()
