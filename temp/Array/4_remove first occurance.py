import array

def remove_first_occurrence(arr, element):
    """
    Description:
      Removes the first occurrence of a specified element from the given array.

    Parameters:
      arr (array): An array of integers.
      element (int): The element to remove.

    Returns:
      array: The array after removing the first occurrence of the specified element.
    """
    try:
        arr.remove(element)
    except ValueError:
        print(f"Element {element} not found in the array.")
    return arr

def main():
    arr = array.array("i", [1, 2, 3, 2, 4, 2, 5])
    element = 2
    print("Original array:", arr)
    print(f"Array after removing the first occurrence of {element}:", remove_first_occurrence(arr, element))

if __name__ == "__main__":
    main()
