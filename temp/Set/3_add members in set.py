"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to add member(s) in a set
"""
def adding_members_in_set():
  """
  Description:
      This function adds member in set
  Parameters:
      none
  Return:
      none
"""
  fruits = {'banana', 'orange', 'mango', 'lemon'}
  print(f"Original set {fruits}")
  fruits.add('lime')
  print(f"Modified set {fruits}")
def main():
  adding_members_in_set()
if __name__=="__main__":
  main()