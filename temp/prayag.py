# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Input: nums = [2,2,1]
# Output: 1

def repeat_number(input_list):
  for num in range(len(input_list)):
      if input_list[num] not in input_list[:num]+input_list[num+1:]:#
        return num

def main():
  input_list=[2,2,1,1,4]
  print("Non repeated number",repeat_number(input_list))

  
if __name__=="__main__":
  main()