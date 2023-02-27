from typing import Sequence


def main():
    a = '1359'

    print(slice_by_evenness(a))


def slice_by_evenness(sequence: tuple | list) -> list[list[int]]:
    """
    Return sequence that consists of lists of even integers
    alternating with lists of odd integers
    so that the integers keep the beginning order.
    if sequence is empty, return [];
    if there's only 1 resulting group, return that group
    Examples:
         [1, 2, 4, 5, 3, 7, 6, 8] => [[1], [2, 4], [5, 3, 7], [6, 8]]
         [] => []
         [1, 3, 5, 7, 9, 11] => [1, 3, 5, 7, 9, 11]
    """
    if len(sequence) == 0:
        return []

    slices = [[sequence[0]]]
    for prev, next_ in zip(sequence, sequence[1:]):
        if prev % 2 != next_ % 2:  # if evenness alternated, start a new slice
            slices.append([])
        slices[-1].append(next_)  # add the next_ integer to the latest started slice

    if len(slices) == 1:  # if there's only 1 resulting group, return that group
        return slices[0]

    return slices


if __name__ == '__main__':
    main()
