'''
Program : To print the first larger number to the next of the element chosen in the array.
Example :
Given array : arr = [1,2,25,3,42,6]
Output should be : [{1: 2}, {2: 25}, {25: 42}, {3: 42}, {42: -1}, {6: -1}]
If a larger number is found , then in that case put that value after the colon, or if not found then append -1.
For the last element of the array , just append -1.
'''
arr = [1,2,25,3,42,6]
arraylenght = len(arr)

tempList = []

for i in range(0, arraylenght):
    #To get the last element
    checkStatus = False
    tempDict  = {}
    if (arr[i] == arr[arraylenght - 1]):
        tempDict[arr[i]]=-1
    else:
        for j in range(i+1,arraylenght):  
            #Check for the flagValue
            if not checkStatus:
                if arr[j] > arr[i]:
                    tempDict[arr[i]]=arr[j]
                    checkStatus = True

                else:
                    tempDict[arr[i]]=-1
    tempList.append(tempDict)
print(tempList)