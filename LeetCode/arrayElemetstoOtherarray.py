'''
Description: Here we need to convert the individual charcters of the elements of the lts into individual elements of an another list.
NOTE: First element of all the elements of the input array, will be the first elemnt of the output array added as the list.
LeetCode Question URL : https://leetcode.com/problems/delete-columns-to-make-sorted/
'''
# Input Array
inp_array =["abc","bce","cae"]
input_arrayLength = len(inp_array)

# Final Array
final_array = [["a","b","c"],["b","c","a"],["c","e","e"]]

output_array = []
tempArray = []
for i in range(0,input_arrayLength):
    elementsarray = list(inp_array[i].strip())
    tempArray.append(elementsarray)
print(tempArray)
#print(len(tempArray))

for i in range(0,len(tempArray)):
    tempArray2 = []
    for elem in tempArray:
        tempArray2.append(elem[i])
    output_array.append(tempArray2)

print(output_array)

counter = 0

for element in output_array:
    for elem in range(1,len(element)):
        if(ord(element[elem]) < ord(element[elem-1])):
            counter=counter+1
            break
print(counter)