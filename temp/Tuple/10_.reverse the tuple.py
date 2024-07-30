"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :  Python program to reverse a tuple
"""
def reverse_tuple(tpl):
  """
  Description:
      This function check the number is power of 2
  Parameters:
      tpl(tuple): The tuple to be reversed
  Return:
      tuple: reversed tuple
"""
  return tpl[::-1]
def main():
  tpl=(1,2,3,4,4,5,6,6,7)
  print(f"Original tuple :{tpl}")
  print(f"Reverse tuple :{reverse_tuple(tpl)}")
if __name__=="__main__":
  main()