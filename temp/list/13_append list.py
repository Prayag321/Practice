'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :Python program to append a list to the second list
'''
def append_list(lst,new_list):
  """
  Description:
      This function check the number is power of 2
  Parameters:
      num : decimal number 
  Return:
      boolean : true or false
"""

  lst.extend(new_list)
  
  return lst
def main():
  lst = [1,2,4,9,0,7]
  new_list = [9,8,7]
  print(f"Appended list is :{append_list(lst,new_list)}")
if __name__=="__main__":
  main()