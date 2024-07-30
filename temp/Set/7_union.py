"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to create an union of sets
"""
def union_set(python,dragon):
  """
  Description:
      This function perform union
  Parameters:
      python(set):set of alphabets
      dragon(set):set of alphabets
  Return:
      set: union of sets
"""

  return python.union(dragon)
def main():
  python = {'p', 'y', 't', 'h', 'o','n'}
  dragon = {'d', 'r', 'a', 'g', 'o','n'}
  print(python,dragon,sep="\n")
  print(f"Difference between teo set :{union_set(python,dragon)}")
  
if __name__=="__main__":
  main()