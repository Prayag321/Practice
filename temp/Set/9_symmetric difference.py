"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python program to create a symmetric difference
"""
def main():
  # syntax
  st1 = {1, 2, 3, 4}
  st2 = {2, 3}
# it means (A\B)∪(B\A)
  print(f"symmetric difference is {st2.symmetric_difference(st1)}") # {1, 4}
if __name__=="__main__":
  main()