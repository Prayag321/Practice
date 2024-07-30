"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Write a Python program to split a list based on the first character of each word
"""



def split_list_by_first_char(words):
    """
    Description:
        This function splits a list of words into a dictionary where each key is a 
        first character and the corresponding value is a list of words starting with that character.
    Parameters:
        words : list 
            A list of words to be split based on their first character.
    Return:
        result(dict) : 
            A dictionary where keys are first characters and values are lists of words 
            starting with that character.
    """
    result = {}
    for word in words:
      first_char = word[0].lower()
      if first_char in result:
        result[first_char].append(word)
      else:
        result[first_char]= word
    return (result)

def main():
    words = ["prayag","deven","ayush"]
    split_dict = split_list_by_first_char(words)
    for key, value in split_dict.items():
      print(f"{key}: {value}")

if __name__ == "__main__":
    main()
