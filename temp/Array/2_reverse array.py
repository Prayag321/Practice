"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python program to reverse the order of the items in the array.  
"""
import array 
def reverse_order(arr):
  """
    Description:
      Reverses the order of the items in the given array.

    Parameters:
      arr (array): An array of integers.

    Returns:
      array:reverced version of input array
"""
  return arr[::-1]
def main():
  arr = array.array("i",[1,2,3,4,5])
  print("Original array : ",arr)
  print("Reverse array is : ",reverse_order(arr))

if __name__=="__main__":
  main()