"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Write a Python program to get the difference between two lists   
"""
def difference_bet_list(lst1,lst2):
  """
    Description:
      This function returns the difference between two lists, i.e., elements that are in lst1 but notin lst2.
    Parameters:
      lst1 (list) :The first list.
      lst2 (list) :The second list.
    Return:
      list : 
            A list containing elements that are in lst1 but not in lst2.
    """
  return list(set(lst1).difference(set(lst2)))
def main():
  lst1 =["prayag","deven","ayush"]
  lst2 =["prayag","deven"]
  print(difference_bet_list(lst1,lst2))
if __name__=="__main__":
  main()