def sort_dict_by_value(d, ascending=True):
    """
    Description:
      Sorts a dictionary by its values.

    Parameters:
      d (dict): The dictionary to sort.
      ascending (bool): Sort order flag. True for ascending, False for descending.

    Returns:
      dict: A new dictionary sorted by its values.
    """
    items = list(d.items())

    for i in range(len(items)):
        # Find the index of the minimum or maximum element based on the order
        idx = i
        for j in range(i + 1, len(items)):
            if ascending:
                if items[j][1] < items[idx][1]:
                    idx = j
            else:
                if items[j][1] > items[idx][1]:
                    idx = j
        items[i], items[idx] = items[idx], items[i]

    return dict(items)

def main():
    my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5, 'elderberry': 4}

    print("Original dictionary:", my_dict)
    
    ascending_sorted_dict = sort_dict_by_value(my_dict, ascending=True)
    print("Dictionary sorted by value (ascending):", ascending_sorted_dict)
    
    descending_sorted_dict = sort_dict_by_value(my_dict, ascending=False)
    print("Dictionary sorted by value (descending):", descending_sorted_dict)

if __name__ == "__main__":
    main()
