"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to create an difference of sets
"""
def difference_set(python,dragon):
  """
  Description:
      This function perform difference
  Parameters:
      python(set):set of alphabets
      dragon(set):set of alphabets
  Return:
      set: difference of sets
"""

  return python.difference(dragon)
def main():
  python = {'p', 'y', 't', 'h', 'o','n'}
  dragon = {'d', 'r', 'a', 'g', 'o','n'}
  print(python,dragon,sep="\n")
  print(f"Difference between teo set :{difference_set(python,dragon)}")
  
if __name__=="__main__":
  main()