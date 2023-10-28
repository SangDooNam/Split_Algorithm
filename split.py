from text import text_1


def split(arr, container=None, partition_point=" "):
    """
    Recursively divides an input list or string based on a specified partition point.

    This function iterates through the input array (arr) and splits it every time it encounters
    the specified partition point. The resulting sub-arrays or sub-strings are then added to a container list.

    Parameters:
    - arr (list or str): The input array or string to be split.
    - container (list, optional): A list to store the resulting sub-arrays or sub-strings.
                                If not provided, a new list is initialized. Default is None.
    - partition_point (any, optional): The element in the array or character in the string at which to split.
                                    Default is a space character (' ').

    Returns:
    - list: A list containing the sub-arrays or sub-strings resulting from the split.

    Examples:
    - split("Hello World") returns ['Hello', 'World']
    - split([1, 2, 3, ' ', 4, 5]) returns [[1, 2, 3], [4, 5]]
    """
    if container is None:
        container = []
    index = -1
    for space in arr:
        index += 1
        if space == partition_point:
            container.append(arr[:index])
            return split(arr[index + 1 :], container, partition_point)
    container.append(arr)
    return container


result = split(text_1, partition_point="e")
print(result)
