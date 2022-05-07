'''

FORMATTED NUMBER
Have the function FormattedNumber(strArr) take the strArr parameter being passed, which will 
only contain a single element, and return the string true if it is a valid number that 
contains only digits with properly placed decimals and commas, otherwise return the string false. 

For example: if strArr is ["1,093,222.04"] then your program should return the string true, 
but if the input were ["1,093,22.04"] then your program should return the string false. 

The input may contain characters other than digits.

Examples
Input: ["0.232567"]
Output: true
Input: ["2,567.00.2"]
Output: false

'''

def FormattedNumber(strArr):
  str_len = len(strArr)
  index = str_len - 1
  count_decimal = 0
  count_digit = 0
  
  while index >= 0:

    if strArr[index].isdigit():
      count_digit += 1
    elif strArr[index] == '.':
      if count_digit != 0:
        count_decimal += 1
        count_digit = 0
      else:
        #if '.' found before any digits
        return False
    elif strArr[index] == ',':
      if count_digit == 3 and count_decimal <=1:
        count_digit = 0
      else:
        #if ',' found before 3 digits
        return False
    else:
      #if not a digit
      return False

    #if more that 2 decimals found
    if count_decimal > 1:
      return False
    #base decrement
    index -= 1
  return True

# keep this function call here 
strList = input()
print(FormattedNumber(strList[0]))

# Input:    ["0.232567"]    --> True
# Input:    ["2,567.00.2"]  --> False
