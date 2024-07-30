
# 13 --> 10 --> 1
# 15 ---> 1^2 + 5^2 = 26
def happy_number(number):
  repeated_number=[]

  while number!=1:
    
    if square_number(number) in repeated_number:
      return f"nahi he"
    
    number = square_number(number)
    repeated_number.append(number) 


  return f"he"


def square_number(number):
  digit=0
  result=0
  while number>0:
    digit=number%10
    result = result+digit**2
    number//=10
  return(result)


def main():
  number=13
  print(happy_number(number))

if __name__=="__main__":
  main()