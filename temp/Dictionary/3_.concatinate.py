"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python script to concatenate following dictionaries to create a new one
"""
def concatenate(dic1,dic2,dic3):
  """
    Description:
      Concatenates three dictionaries into a new dictionary. The resulting dictionary contains all key-value pairs from the input dictionaries.

    Parameters:
      dic1 (dict): The first dictionary to concatenate.
      dic2 (dict): The second dictionary to concatenate.
      dic3 (dict): The third dictionary to concatenate.

    Returns:
      dict: A new dictionary containing all key-value pairs from the input dictionaries. 
    """
  dic1 = dic1.items()
  dic2 = dic2.items()
  dic3 = dic3.items()
  new_dict = []
  new_dict.extend(dic1)
  new_dict.extend(dic2)
  new_dict.extend(dic3)
  return (dict(new_dict))

  
def main():
  dic1={1:10, 2:20}  
  dic2={3:30, 4:40}  
  dic3={5:50, 6:60} 
  new_dict = concatenate(dic1,dic2,dic3)

if __name__=="__main__":
  main()