'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :Python program to create the colon of a tuple
'''
def main():
  tpl=tuple(["prayag",22,True])
  print(f"The original tuple:{tpl}")
  clone_tuple = tuple([*tpl])
  print(f"The clone tuple is:{clone_tuple}")
if __name__=="__main__":
  main()