'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :Python program to unpack a tuple in several variables.
'''

def main():
  tlp=tuple(["prayag",22,True])
  name,age,smart = tlp
  print("We just create a tuple",tlp)
  print(f"Name:{name} \nAge:{age} \nSmart: {smart}")
if __name__=="__main__":
  main()