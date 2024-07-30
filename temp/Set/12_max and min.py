"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program to find maximum and the minimum value in a set
"""
def max_min(st):
  """
  Description:
      This function check the maximum and the minimum value in a set
  Parameters:
      st(set):set of numbers
  Return:
      max,min(int):maximum and the minimum value in a set
"""
  st=list(st)
  max=st[0]
  min=st[0]
  for elem in st:
    if elem>max:
      max=elem
    else:
      min=elem

  return max,min
def main():
  st = {1, 2, 1, 3, 4}
  max,min=max_min(st)
  print(f"Maximum number is {max}\nMinium number is {min}")
if __name__=="__main__":
  main()