"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python script to add a key to a dictionary. 
"""
def main():
  user_data = {
    "name":"Prayag",
    "age":22
    }

  print("Befor adding: ",user_data)
  user_data["smart"]=True
  print("After adding: ",user_data)

if __name__=="__main__":
  main()