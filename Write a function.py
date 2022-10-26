# The function must return a Boolean value (True/False). Output is handled by the provided code stub.
# Sample Input 0
# 1990
# Sample Output 0
# False
# Explanation 0
# 1990 is not a multiple of 4 hence it's not a leap year.

def is_leap(year):
    leap=False
    if year%400==0:
         leap=True
    elif year%100==0:
         leap=False
    elif year%4==0:
         leap=True
    return leap
year=int(input())
print(is_leap(year))
