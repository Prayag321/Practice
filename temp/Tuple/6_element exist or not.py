"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to check whether an element exists within a tuple
"""
def element_exist(tpl,number):
  """
    Description:
        This function checks whether an element exists within a tuple.
    Parameters:
        tpl : tuple
            The tuple in which to check for the element.
        number : any
            The element to check for in the tuple.
    Return:
        boolean : 
            True if the element exists in the tuple, otherwise False.
    """
  if number in tpl:
    return True
  else:
    return False
def main():
  number = 5
  tpl=(1,2,3,4,4,5,6,6,7)
  print(f"Original tuple is :{tpl}")
  print(f"{number} in tuple :{element_exist(tpl,number)}")
if __name__=="__main__":
  main()