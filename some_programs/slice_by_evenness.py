from typing import Sequence


def main():
    a = [1, 1, 2, 2, 2, 2, 3, 3, 43, 4, 34, 4, 54, 23, 74, 74, 74, 769]

    print(slice_by_evenness(a))


def slice_by_evenness(seq: Sequence[int]) -> list[list[int]]:
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
    if len(seq) == 0:
        return []

    slices = [[seq[0]]]
    for prev, next_ in zip(seq, seq[1:]):
        if prev % 2 != next_ % 2:  # if evenness alternated, start a new slice
            slices.append([])
        slices[-1].append(next_)  # add the next_ integer to the latest started slice

    if len(slices) == 1:  # if there's only 1 resulting group, return that group
        return slices[0]

    return slices


if __name__ == '__main__':
    main()
