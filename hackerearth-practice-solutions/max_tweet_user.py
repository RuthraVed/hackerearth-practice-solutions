# Given a list of tweets, write a program to find
# the user who has tweeted the most.
#
# Note: If multiple users are having the same number of tweets,
# then print all the users in alphabetical order of user names.


from collections import Counter

def max_tweet_user(tweets_list):
    tweets_list.sort()  # Sorts the list alphabetically
    tweets_count_dict = dict(Counter(tweets_list))  # Prepares a dict of tweets-count per individual
    
    max_count = 0
    display_list = []

    # First iteration to find the max_count
    for user, count in tweets_count_dict.items():
        if count > max_count:
            max_count = count

    # Second iteration to print the user as desired by the program
    for user, count in tweets_count_dict.items():
        if count == max_count:
            display_list.append(user + ' ' + str(count))
    
    return display_list


if __name__ == "__main__":

    final_display_list = []
    
    T = int(input())    # Number of testcases    
    for i in range(T):
        tweets_list = []
        N = int(input())    # Number of tweets per testcase
        for j in range(N):
            tweets_list.append(input().split(' tweet')[0])
        final_display_list += max_tweet_user(tweets_list)
    
    for output in final_display_list:
        print(output)


'''    TestCases

Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3 
        (PASSED).
------------------

Sample 2:
Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output
kohli 2
sachin 2
sehwag 2 
        (PASSED).
------------------


Sample 3:
Input 
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

Output
sachin 2
sehwag 2
dhoni 4
        (PASSED).
------------------

Sample 4:
Input
3
4
sehwag tweet_id_2
sehwag tweet_id_4
sachin tweet_id_1
sachin tweet_id_3
7
sehwag tweet_id_10
sehwag tweet_id_11
kohli tweet_id_12
sachin tweet_id_13
sachin tweet_id_14
sachin tweet_id_1
sehwag tweet_id_4
5
sachin tweet_id_2
kohli tweet_id_4
kohli tweet_id_1
kohli tweet_id_3
sachin tweet_id_5

Output
sachin 2
sehwag 2
sachin 3
sehwag 3
kohli 3
        (PASSED).
------------------
'''
