# The Unlucky 13 - with caching

cache = {}
mod = 1000000009
def total_no_of_strings_without_13(n):

    # Maintaining two caches to comply with memory constrains 
    if n < 50000000:
        if n  in cache:
            return cache[n]
        
        # Base conditions
        if n == 0:
            cache[n] = 1
            return cache[n]
        if n == 1:
            cache[n] = 10
            return cache[n]
        
        # Eg. If N is 2, then we will have the problem divided as below
        temp1 = total_no_of_strings_without_13(n//2)    # As N is 1, it returns 10
        temp2 = total_no_of_strings_without_13((n//2)-1)    # As N is 0, it returns 1

        # A case when the problem can be divided into even parts. Eg. If N is 2 or 4 or so on...
        if (n%2) == 0:
            cache[n] = (temp1 * temp1 - temp2 * temp2) % mod  # Originally, x*x - y*y
        # A case when the problem divides into odd parts.
        else:
            # Eg. If N is 3, then we will have the problem divided as below
            temp3 = total_no_of_strings_without_13((n//2)+1) # As N is 2, it returns 99
            cache[n] = (temp1 * (temp3 - temp2)) % mod   # Originally, x*y - x*z
        return cache[n]

    else:
        if n  in cache2:
            return cache2[n]
        
        temp1 = total_no_of_strings_without_13(n//2)
        temp2 = total_no_of_strings_without_13((n//2)-1)

        if (n%2) == 0:
            cache2[n] = (temp1 * temp1 - temp2 * temp2) % mod        
        else:
            temp3 = total_no_of_strings_without_13((n//2)+1)
            cache2[n] = (temp1 * (temp3 - temp2)) % mod
        return cache2[n]


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        cache2 = {}
        print(total_no_of_strings_without_13(N))
