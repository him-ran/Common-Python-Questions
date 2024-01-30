if __name__ == '__main__':
    #n = int(input())
    n=5
    arr = map(int, input().split())
    simpleList=[]
    for i in arr:
        simpleList.append(i)
    simpleList=(sorted(simpleList,reverse=True))
    for i in range(0,len(simpleList)):
        if(simpleList[i] != simpleList[i+1]):
            print(simpleList[i+1])
            break



