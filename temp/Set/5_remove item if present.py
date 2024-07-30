"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to remove an item from a set if it is present in the set
"""
def remove_item_if_present(fruits,item):
  """
  Description:
      This function remove item if present in set
  Parameters:
      fruits(set):set of fruits 
      item(int):value to be remove
  Return:
      none
"""
  print(f"Original set {fruits}")

  if item in fruits:
    fruits.remove(item)
    
  print(f"Remove if present is :{fruits}")

def main():
  fruits = {'banana', 'orange', 'mango', 'lemon'}
  item = "orange"
  remove_item_if_present(fruits,item)
if __name__=="__main__":
  main()