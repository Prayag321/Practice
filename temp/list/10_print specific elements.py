"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to print a specified list after removing the 0th, 4th and 
             5th elements.    
"""
def remove_elements(lst):
  """
    Description:
      This function removes the 0th, 4th, and 5th elements from the given list.
    Parameters:
      lst (list) :The list from which the specified elements are to be removed.
    Return:
      new_list(list) : The modified list after removing the specified elements.
    """
  new_list=[elem for elem in lst if lst.index(elem)!=0 and lst.index(elem)!=4 and lst.index(elem)!=5]
  return new_list
def main():
   lst = [1,2,4,9,0,7]
   print(remove_elements(lst))
if __name__=="__main__":
  main()