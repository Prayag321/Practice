"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to create a dictionary from a string.  
Note: Track the count of the letters from the string.
"""
def dictionary_from_string(string):
  """
  Description:
      This function check the number is power of 2
  Parameters:
      num : decimal number 
  Return:
      boolean : true or false
"""
  new_dict = {}
  for elem in string:
    if elem in new_dict:
      new_dict[elem]+=new_dict[elem]
    else:
      new_dict[elem] = 1
  return new_dict

  
def main():
  string = "Prayag"
  result_dict = dictionary_from_string(string)
  print(f"The result is {result_dict}")
if __name__=="__main__":
  main()