"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python script to iterate dict
"""
def iterate_over_dict(d):
    """
    Description:
      Iterates over a dictionary and prints its keys, values

    Parameters:
      d (dict): The dictionary to iterate over.

    Returns:
      None
    """
    # Iterate over key-value pairs
    print("Key-Value Pairs:")
    for key, value in d.items():
        print(f"{key}: {value}")

def main():
  sample_dict = {
    'name': 'Prayag',
    'age': 22,
    'city': 'Panvel',
    'occupation': 'Engineer'
  }
  
  iterate_over_dict(sample_dict)

if __name__ == "__main__":
    main()
