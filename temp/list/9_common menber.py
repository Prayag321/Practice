'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Write a Python function that takes two lists and returns True if they have at 
    least one common member.  
'''
def compare_list(lst1,lst2):
  """
  Description:
      This function check the number is power of 2
  Parameters:
      num : decimal number 
  Return:
      boolean : true or false
"""
  for elem in lst1:
    if elem in lst2:
      return True
  return False
def main():
  lst1 = [9,2,3]
  lst2 = [1,4,6]
  print(compare_list(lst1,lst2))
if __name__=="__main__":
  main()