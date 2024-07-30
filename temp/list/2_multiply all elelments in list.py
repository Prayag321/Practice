'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program  to multiply all the items in a list
'''
def mul_of_list(lst):
  """
  Description:
      This function add all elements in the list
  Parameters:
      lst(list): List of numbers
  Return:
      mul(int): Multiplication of all elements in list
"""
  mul = 1
  for elem in lst:
    mul*=elem
  
  return mul

  pass
def main():
  lst = [1,2,4]
  print(f"Multiplication of all elements is : {mul_of_list(lst)}")
if __name__=="__main__":
  main()