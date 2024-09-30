def index_all(search_list, item):
    """
    Finds all occurrences of an item within a nested list.

    Args:
        search_list: The nested list to search.
        item: The item to search for.

    Returns:
        A list of lists, where each inner list represents the indices of an occurrence of the item.
    """

    indices = []
    stack = [(search_list, [])]

    while stack:
        current_list, current_index = stack.pop()

        for i, element in enumerate(current_list):
            if isinstance(element, list):
                stack.append((element, current_index + [i]))
            elif element == item:
                indices.append(current_index + [i])

    return indices

if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]