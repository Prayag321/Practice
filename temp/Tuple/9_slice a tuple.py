'''
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to slice a tuple 
'''
def slice_tuple(tpl,start,end):
  """
    Description:
        This function slices a tuple from the specified start index to the end index.
    Parameters:
        tpl (tuple):  The tuple to be sliced.
        start (int):  The start index for slicing (inclusive).
        end (int):  The end index for slicing (exclusive).
    Return:
        tuple :  The sliced tuple.
    """
  return tpl[start-1:end] # cause its indexing
def main():
  start = 1
  end = 5
  tpl=(1,2,3,4,4,5,6,6,7)
  print(f"Sliced tuple is from {start} to {end} is {slice_tuple(tpl,start,end)}")
if __name__=="__main__":
  main()