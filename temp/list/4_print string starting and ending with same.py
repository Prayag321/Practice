'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program  to count the number of strings where the string length 
    is 2 or more and the first and last character are same from a given list of strings. 
'''
def print_words(string_list):
  """
  Description:
      This function counts words who has srats and ends with same if lengths is greater than 2
  Parameters:
      string_list(list):List of strings/words
  Return:
      count(int): count of words who has srats and ends with same
"""
  count = 0
  for word in string_list:
    if(len(word)>2):
      if(word.startswith(word[-1])):
        count+=1
  return count
  
def main():
  string_list=['abc', 'xyz', 'aba', '1221'] 
  print(print_words(string_list))
if __name__=="__main__":
  main()