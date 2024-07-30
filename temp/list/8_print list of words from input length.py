'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Write a Python program to find the list of words that are longer than n from a 
    given list of words.  
'''
def longer_string(word_list,n):
  """
  Description:
      This function check word length longer than user input
  Parameters:
      word_list(list):List of word from the user
      n(int): Input length
  Return:
      count(int): count of words that are longer than the input length
"""
  count = 0
  for word in word_list:
    if(len(word)>n):
      count+=1
  return count
      
def main():
  user_input_string = input("Enter sentence")
  word_list = user_input_string.split(" ")
  user_number = int(input("Enter a number :"))
  print(f" Number of words greater than user input is:{longer_string(word_list,user_number)}")
if __name__=="__main__":
  main()