'''
    This is the code to generate the fibonacci series. : 0, 1,1,2,3,5,8,......
'''

uptoNum = int(input("Upto how many numbers: "))
first_num= 0
second_num = 1
for i in range(0, uptoNum):
    if i == 0:
        print(0,end=",")
    else:
        sum = (first_num + second_num)
        second_num = first_num
        first_num = sum
        print(sum,end=",")
        
    
        
        