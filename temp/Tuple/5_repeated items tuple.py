'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title :Python program to find the repeated items of a tuple
'''
def repeted_items(tpl):
  """
    Description:
        This function finds and returns the repeated items in a tuple.
    Parameters:
        tpl (tuple):The tuple in which to find repeated items.
    Return:
        set : A set containing the repeated items.
    """
  repeted_items = []
  for i in range(len(tpl)):
    if tpl[i] in tpl[:i]+tpl[i+1:]:
      repeted_items.append(tpl[i])
  return set(repeted_items)
def main():
  tpl=(1,2,3,4,4,5,6,6,7)
  print(repeted_items(tpl))
if __name__=="__main__":
  main()