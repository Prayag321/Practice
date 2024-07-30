import array

def count_occurrences(arr, element):
    """
    Description:
      Counts the number of occurrences of a specified element in the given array.

    Parameters:
      arr (array): An array of integers.
      element (int): The element to count occurrences of.

    Returns:
      int: The number of occurrences of the specified element in the array.
    """
    return arr.count(element)

def main():
    arr = array.array("i", [1, 2, 3, 2, 4, 2, 5])
    element = 2
    print("Array:", arr)
    print(f"Number of occurrences of {element}:", count_occurrences(arr, element))

if __name__ == "__main__":
    main()
