'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to clone or copy a list.
'''
def main():
  lst = [1,1,2,2,4]
  clone_list = [*lst]
  print(f"The copy of list {lst} is: {clone_list}")

if __name__=="__main__":
  main()