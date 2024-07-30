'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to get the smallest number from a list
'''
def smallest_number(lst):
  """
  Description:
      This function check the smallest number
  Parameters:
      lst(list) : List of numbers
  Return:
      smallest_number(int): smallest number in list
"""
  smallest_number= lst[0]
  for index in range(len(lst)):
    if smallest_number>lst[index]:
      smallest_number = lst[index]
  return smallest_number

def main():
  lst = [1,2,4]
  print(f"Smallest of all elements is : {smallest_number(lst)}")
if __name__=="__main__":
  main()