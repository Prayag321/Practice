"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to iteration over sets
"""
def iterate_set(user_set):
  """
  Description:
    This function iterate the items in set
  Parameters:
    user_set(set) : set of items/numbers 
  Return:
    none
"""
  for elem in user_set:
    print(elem)

def main():
  user_set = {1,2,3,4}  
  iterate_set(user_set)

if __name__=="__main__":
  main()