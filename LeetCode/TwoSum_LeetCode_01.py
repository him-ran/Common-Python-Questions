'''
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
LeetCode Question URL: https://leetcode.com/problems/two-sum/
'''

nums = [12,2,7,15]
target = 27
valueFound=False
nums_length = len(nums)
outputArray=[]

for i in range(0,nums_length):
    currentIndexValue=i
    for j in range(currentIndexValue+1, nums_length):
        if((nums[currentIndexValue]+nums[j]) == target):
            outputArray.append(currentIndexValue)
            outputArray.append(j)
print(outputArray)
