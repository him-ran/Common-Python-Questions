'''
Description: Given a string s, find the length of the longest substring without repeating characters.
Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
LeetCode Question URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

# Input String
s="pwwkew"
#s="bbbbb"
# substring=''
# substringArray=[]
# count=0
# for i in s:
#     print(count)
#     if(substring == ''):
#         substring = substring + i
#     else:
#         # print("Inside the loop for " + str(i))
#         if((i == substring[0])):
#             print("In for "+i)
#             if(len(substringArray) < 0):
#                 substringArray.append(substring)
#             else:
#                 if(substring not in substringArray):
#                     substringArray.append(substring)
#         else:
#             substring=''
#         substring = substring+i
#     count=count+1
#     #print(substring)
# maxlength = 0
# for elem in substringArray:
#     if (len(elem) > maxlength):
#         maxlength=len(elem)
# print(substringArray)
# print(maxlength)
#print(len(substringArray[0]))
#return (len(substringArray[0]))
#Base condition
if s == "":
    print (0)
# Starting index of window
start = 0
# Ending index of window
end = 0
# Maximum length of substring without repeating characters
maxLength = 0
# Set to store unique characters
unique_characters = set()
# Loop for each character in the string
while end < len(s):
    if s[end] not in unique_characters:
        unique_characters.add(s[end])
        end += 1
        maxLength = max(maxLength, len(unique_characters))
    else:
        unique_characters.remove(s[start])
        start += 1
print (maxLength)