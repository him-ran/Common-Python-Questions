if __name__ == '__main__':
    #x = int(input())
    #y = int(input())

    lst = []
    temp_list = []
    for temp1 in range(0,x+1):
        for temp2 in range(0,y+1):
            for temp3 in range(0,z+1):
                sum = (temp1+temp2+temp3)
                if ( sum != k):
                    temp_list.append(temp1)
                    temp_list.append(temp2)
                    temp_list.append(temp3)
                    lst.append(temp_list)
                    temp_list=[]
    print(lst)
