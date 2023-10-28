# Split Algorithm

The split algorithm is a Python function designed to divide a given list or string based on a specified partition point. It is implemented using a recursive approach, ensuring efficiency and simplicity in handling various types of input.

## How It Works

The `split` function takes three parameters:

1. `arr`: The input array or string to be split.
2. `container` (optional): A list to store the resulting sub-arrays or sub-strings. A new list is initialized if not provided.
3. `partition_point` (optional): The element in the array or character in the string at which to split. The default is a space character (' ').

The function iterates through the input, splitting it every time it encounters the partition point, and the resulting parts are added to the container list. The process is applied recursively until the entire input has been processed.

## Usage Example

```python
text_1 = "Hello World"
result = split(text_1)
print(result)  # Output: ['Hello', 'World']