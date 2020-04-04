if __name__ == '__main__':
    #For the storage of the entries
    studentsMainList=[]
    #For splittign the values of the name and the score as differnt entities.
    for _ in range(int(input())):
        name = input()
        score = float(input())
        smallList=[]
        smallList.append(name)
        smallList.append(score)
        studentsMainList.append(smallList)
    #Variable definition
    marksList= []
    secSmallest = 0
    nameList = []
    #To fetch only the marks , for the entries done.
    for i in studentsMainList:
        marksList.append(i[1])
    marksList = sorted(marksList)
    #logic to print the second smallest number of the array
    marksListLength=len(marksList)
    for i in range(0, marksListLength - 1):
        if marksList[i] != marksList[i+1]:
            secSmallest=(marksList[i+1])
            break
    #To print the name of students who have the same second smallest score
    for i in studentsMainList:
        marks=i[1]
        if marks == secSmallest:
            nameList.append(i[0])
    nameList = sorted(nameList)
    for i in nameList:
        print(i)
