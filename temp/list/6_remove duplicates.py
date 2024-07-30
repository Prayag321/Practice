'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :  Python program to remove duplicates from a list
'''
def remove_duplicaates(lst):
  """
  Description:
      This function checks duplicates and remove
  Parameters:
      lst(list) : List of numbers
  Return:
      lst(list) : unique list 
"""
  for elem in lst:
    if elem in lst[:lst.index(elem)]+lst[lst.index(elem)+1:]:
      lst.remove(elem)
  return lst
def main():
  lst = [1,1,2,2,4]
  print("The modified list is",remove_duplicaates(lst))
if __name__=="__main__":
  main()