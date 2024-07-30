"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python program to remove item(s) from set 
"""
def remove_item_in_set():
  """
  Description:
      This function remove item(s) from set 
  Parameters:
      none
  Return:
      none
"""
  fruits = {'banana', 'orange', 'mango', 'lemon'}
  print(f"Original set {fruits}")

  fruits.pop()# removes a random item from the set
  print(f"Modified set {fruits}")

def main():
  remove_item_in_set()
if __name__=="__main__":
  main()