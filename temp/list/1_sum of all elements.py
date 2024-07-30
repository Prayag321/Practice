'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program  to sum all the items in a list
'''
def sum_of_list(lst):
  """
  Description:
      This function add all elements in the list
  Parameters:
      lst(list): List of numbers
  Return:
      sum(int): Sum of all elements in list
"""
  sum = 0
  for elem in lst:
    sum+=elem
  
  return sum

  pass
def main():
  lst = [1,2,4,6,7,9,34,23,89]
  print(f"sum of all elements is : {sum_of_list(lst)}")
if __name__=="__main__":
  main()