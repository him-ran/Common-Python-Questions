'''
Description: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
LeetCode Question URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

# First Array
nums1=[1,2]
# Second Array
nums2 = [3,4]

# Merging the array
for element in nums2:
    nums1.append(element)

# Sorting the array
nums1.sort()
mergedArrayLength=len(nums1)

# Incase there are even elements in the merged array
if((mergedArrayLength%2) == 0):
    midValueIndex=int(mergedArrayLength/2)
    indexNextTomid=midValueIndex-1
    median=float((nums1[midValueIndex]+nums1[indexNextTomid])/2)
else:
# Incase there are even elements in the merged array
    medianIndexValue=int(mergedArrayLength/2)
    #print(medianIndexValue)
    #print("Median is: " + str(float(nums1[medianIndexValue],0.2f)))
    median=float(nums1[medianIndexValue])

#return median
print(median)
