"""

EVEN PAIRS
Have the function EvenPairs(str) take the str parameter being passed and 
determine if a pair of adjacent even numbers exists anywhere in the string. 
If a pair exists, return the string true, otherwise return false. 

For example: if str is "f178svg3k19k46" then there are two even numbers 
at the end of the string, "46" so your program should return the string true. 
Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so 
your program should return the string true.

Examples
Input: "3gy41d216"
Output: true
Input: "f09r27i8e67"
Output: false

"""

def EvenPairs(strParam):
    
    str_len = len(strParam)
    index = 0
    
    while index < str_len:
        digits = ''
        count = 0

        for j in range(index, str_len):            
            #Checking if digit or not
            if strParam[j].isdigit():
                digits+=strParam[j]
                if int(digits)%2==0:    
                    count+=1
            else:
                index=j
                #To avoid going till end each time
                break             
            #Since else-control will not be explored
            #Thus, for when string ends with digit
            if j == str_len-1:  
                index=j
            
            if count>=2:    
                return True
        
        #Whatever be case, base increment will happen
        index+=1
    return False

if __name__ == '__main__':
    print(EvenPairs('f178svg3k19k46'))  #True
    print(EvenPairs('7r5gg812'))    #True
    print(EvenPairs('3gy41d216'))   #True
    print(EvenPairs('f09r27i8e67')) #False
    print(EvenPairs('fdfs1386eretre'))  #True
