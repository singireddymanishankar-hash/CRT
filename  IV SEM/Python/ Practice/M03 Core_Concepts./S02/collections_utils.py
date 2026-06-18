def create_list(*elements):
    """Create a list from the given elements."""
    return list(elements)


def access_first(lst):
    """Access the first element of a list."""
    return lst[0]


def access_last(lst):
    """Access the last element of a list."""
    return lst[-1]


def repeat_list(lst, times):
    """Repeat a list a given number of times."""
    return lst * times


def remove_element(lst, element):
    """Remove the first occurrence of an element from a list."""
    result = lst.copy()
    result.remove(element)
    return result


def slice_list(lst, start, end):
    """Slice a list from start to end (exclusive)."""
    return lst[start:end]
