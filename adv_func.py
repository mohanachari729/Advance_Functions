# #function definition
# def add(a,b):
#     return a+b
# obj = add(1,2)
# print(obj)

# #lambda argument : expression
# result = lambda a,b:a+b
# print(result(1,2))

# # #lambda argument : expression
# result = lambda a,b : a*b
# print(result(4,4))

# #filter advance function
# result = filter(lambda i : i%2==0 , [1, 2, 3 ,4, 5 ,6 ,7 ,8 ,9 ] )
# print(list(result))
# #5
# list1 = [1 ,2 ,3 ,4 ,5 ,6, 7 ,8 ,9]
# empty = []
# for i in list1 :
#     if i%2 == 0 :
#         empty.append(i)
# print(empty)

# ##6 filter
# list1 = [1 ,2 ,3 ,4 ,5 ,6, 7 ,8 ,9]
# def even(i):
#     return i%2 == 0 
# result = filter(even,(list1))
# print(list(result))

# ##7 map function
# list1 = [1,2,3,4]
# empty = []
# for i in list1:
#     square = i*2
#     empty.append(square)
# print(empty)

# ##8 
# list1 = [1,2,3,4]
# def mul(i):
#     return i*2 
# result = map(mul,list1)
# print(list(result))

# ##9
# result = map(lambda i : i*2 , [1,2,3,4])
# print(list(result))

# ## functool
# def multi(x ,y):
#     return x*y
# # print(multi(12,2))
# from functools import reduce
# result = reduce(multi,[1,1,2,3,4])
# print(result)

##generator function
def sample():
    yield 1+1
    yield 2+2
    yield 3+4
obj = sample()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())



