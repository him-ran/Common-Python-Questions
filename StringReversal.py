#String Reversal Using Python3
name = "Himanshu"
list1 = list(name)
# print(type(list1))
list1.reverse()
print(list1)

#Check for Palindrome
# Python3 program for the
# practical application of reverse()

# store a copy of list
copiedList = list1.copy()

# reverse the list
copiedList.reverse()

# compare reversed and original list
if list1 == copiedList:
    print("Palindrome")
else:
    print("Not Palindrome")

#NumberReversal
number=12345
# using map()
# to convert number to list of integers
res = list(map(int, str(number)))

res.reverse()
print(res)
# Converting integer list to string list
s = [str(i) for i in res]

# Join list items using join()
rev = int("".join(s))

print(rev)
print(type(rev))
