"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python program to remove a key from a dictionary  
"""
def remove_key(dictionary, key_to_remove):
    """
    Description:
      this function removes a specified key from a dictionary.

    Parameters:
      dictionary (dict): The dictionary from which to remove the key.
      key_to_remove (hashable): The key to remove from the dictionary.

    Returns:
      dict: modified dict
    """
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
    return dictionary

def main():
    sample_dict ={
    "name":"Prayag",
    "age":22
    }

    print("Original Dictionary:")
    print(sample_dict)

    key = 'age'

    updated_dict = remove_key(sample_dict, key)

    print("Updated Dictionary:")
    print(updated_dict)

if __name__ == "__main__":
    main()
