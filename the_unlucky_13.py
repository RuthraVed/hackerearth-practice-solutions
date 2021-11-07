# The Unlucky 13 - without any caching

def total_no_of_strings_without_13(n):
    mod = 1000000009
    
    # Base conditions
    if n == 0:
        return 1
    if n == 1:
        return 10
    
    # Eg. If N is 2, then we will have the problem divided as below
    temp1 = total_no_of_strings_without_13(n//2)    # As N is 1, it returns 10
    temp2 = total_no_of_strings_without_13((n//2)-1)    # As N is 0, it returns 1

    # A case when the problem can be divided into even parts. Eg. If N is 2 or 4 or so on...
    if (n%2) == 0:
        res = (temp1 * temp1 - temp2 * temp2) % mod  # Originally, x*x - y*y
    
    # A case when the problem divides into odd parts.
    else:
        # Eg. If N is 3, then we will have the problem divided as below
        temp3 = total_no_of_strings_without_13((n//2)+1) # As N is 2, it returns 99
        res = (temp1 * (temp3 - temp2)) % mod   # Originally, x*y - x*z

    return res

if __name__ == "__main__":
    # T = int(input())
    # for i in range(T):
    #     N = int(input())
    #     print(total_no_of_strings_without_13(N))

    print(total_no_of_strings_without_13(4))