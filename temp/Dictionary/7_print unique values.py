"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python script to print all unique values in a list of dictionaries.
"""

def extract_unique_values(data):
    """
    Description:
      Extracts all unique values from a list of dictionaries.

    Parameters:
      data (list of dict):dictionarie containing key-value pairs.

    Returns:
      set: A set of unique values found in the dictionaries.
    """
    unique_values = set(data.values())
    return unique_values

def main():
    sample_data ={
      1:1,
      2:3,
      3:1
    }

    print("Sample Data:")
    print(sample_data)

    unique_values = extract_unique_values(sample_data)

    print("Unique Values:")
    print(unique_values)

if __name__ == "__main__":
    main()
