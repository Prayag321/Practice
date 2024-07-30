"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to create an array of 5 integers and display the array items. Access individual element through indexes. 
"""
import array 
def main():
  arr = array.array("i",[1,2,3,4,5])

  for i in range(len(arr)):
    print(f"{arr[i]}",end=" ")

if __name__=="__main__":
  main()