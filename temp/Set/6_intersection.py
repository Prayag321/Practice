"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to create an intersection of sets
"""
def intersection_set(python,dragon):
  """
  Description:
      This function perform intersection
  Parameters:
      python(set):set of alphabets
      dragon(set):set of alphabets
  Return:
      set: intersection of sets
"""

  return python.intersection(dragon)
def main():
  python = {'p', 'y', 't', 'h', 'o','n'}
  dragon = {'d', 'r', 'a', 'g', 'o','n'}
  print(python,dragon,sep="\n")
  print(f"Intersection between teo set :{intersection_set(python,dragon)}")
  
if __name__=="__main__":
  main()