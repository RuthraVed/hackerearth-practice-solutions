'''

PYTHON AGE COUNTING
In the Python file, write a program to perform a GET request on the 
route https://coderbyte.com/api/challenges/json/age-counting which contains 
a data key and the value is a string which contains items in the 
format: key=STRING, age=INTEGER. 

Your goal is to count how many items exist that have an age equal to 
or greater than 50, and print this final value.

Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2

'''

import requests

URL = "https://coderbyte.com/api/challenges/json/age-counting"

#Counter for age >= 50
count_age = 0

r = requests.get(url = URL)

data_bunch = r.json()['data'].split(',')

for data_set in data_bunch:
  if data_set.find("age=") != -1:
    if int(data_set.split('=')[1]) >= 50:
      count_age += 1

# This single if-control will also work
'''
  if (data_set.find("age=") != -1) and (int(data_set.split('=')[1]) >= 50):
      count_age += 1
'''

print(count_age) #Ans. 128
