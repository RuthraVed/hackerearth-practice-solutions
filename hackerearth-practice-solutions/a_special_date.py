# A special date

def palindrome_date(in_date):
    in_year = in_date[-4:]

    # A valid list of palindrome months, in descending order. 
    possible_months_list = ["90", "80", "70", "60", "50", "40", "30", "21", "20", "11", "10", "01"]

    for month in possible_months_list:
        # Loop for every digit from 0 to 9, in reverse order.
        for i in range(9, -1, -1):
            # Loop to get 3 varieties of each digit,
            # like 92, 91, 90 and so.
            for j in range(2, -1, -1):
                if i == 0:
                    j = j + 1
                p_year = str(month) + str(i) + str(j)
                
                # To get the palindrome date, just smaller than given date
                if in_year >= p_year:
                    p_date = p_year[::-1] + p_year
                    p_day = p_date[:2]
                    in_day = in_date[:2]
                    p_month = p_date[2:4]
                    in_month = in_date[2:4]
                    
                    # A check to see if palindrome date's year is equal to given year.
                    if p_year == in_year:
                        # And if palindrome date's month is greater than given date,
                        # search for next palindrome date
                        if p_month > in_month:
                            continue                        
                        
                        elif p_month == in_month:
                            
                            # If palindrome day is greater than given month,
                            # search for next palindrome date
                            if p_day > in_day:
                                continue
                    # Finally return the palindrome date
                    return p_date
    
    # If no possible palindrome date that comes before given date
    return -1

if __name__ == "__main__":
    from datetime import datetime

    input_date = "07100131"
    print(palindrome_date(input_date))  # Correct output should be: 03 10 0130
    
    """
    # HackerEarth Platform Input
    # ----------------------------------------------------------
    T = int(input())
    for i in range(T):
        input_date = input()
        palindrome_date(input_date)
    # ----------------------------------------------------------
    """

