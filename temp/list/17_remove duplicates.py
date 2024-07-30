'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to remove duplicates from a list of lists
'''
def remove_duplicates(lst):
  """
  Description:
      This function removes duplicate lists from a list of lists.
  Parameters:
      lst (list): list of lists, The list of lists from which duplicates are to be removed.
  Return:
      list : The list of lists after removing duplicates.
  """
  for i in range(len(lst)-1):
    if lst[i] in lst[:i]+lst[i+1:]:
      lst.remove(lst[i])
    
  return lst
def main():
   lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
   print(f"original :{lst}")
   print(f"removed duplicates :{remove_duplicates(lst)}")
if __name__=="__main__":
  main()