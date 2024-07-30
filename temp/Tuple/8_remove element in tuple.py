'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :  Python program to remove an item from a tuple. 
'''
def remove_value(tpl,value):
  """
  Description:
    This function removes the first occurrence of a value from a tuple.
  Parameters:
    tpl (tuple):The tuple from which to remove the value.
    value(any-int):The value to be removed from the tuple.
  Return:
    tuple : The tuple after removing the specified value.
    """
  index = tpl.index(value)
  return tpl[:index]+tpl[index+1:] 
def main():
  tpl=(1,2,3,4,4,5,6,6,7)
  value = 1
  print(remove_value(tpl,value))
if __name__=="__main__":
  main()