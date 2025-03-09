# #square numbers
# result = map(lambda list1 : list1**2 , [6,7,8,9] )
# print(list(result))

# #positive numbers
# result = filter(lambda i : i>0 , [1,2,3,4,5,-6,-7,-8,-9])
# print(list(result))

# #factorization
# from functools import reduce
# n =5
# print(reduce(lambda x , y : x*y, range(1 , n+1)))


##counting vowels
from functools import reduce
string = input("enter the string:")
vowels = "aeiouAEIOU"
count_vowels = reduce(lambda count,char:count+1  if char in vowels else count, string, 0 )
print(count_vowels)




