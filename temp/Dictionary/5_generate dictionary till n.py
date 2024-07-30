"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title :  Python script to generate and print a dictionary that contains a 
    number (between 1 and n) in the form (x, x*x).  
"""
def generate_square_dict(n):
    """
    Description:
      Generates a dictionary till n

    Parameters:
      n (int): User number to add series in dict

    Returns:
      dict: A dictionary with keys as numbers values as their squares.
    """
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict

def main():
    n = 5 
    result_dict = generate_square_dict(n)
    print(f"Sample Dictionary (n = {n}) :")
    print(result_dict)

if __name__ == "__main__":
    main()
