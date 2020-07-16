'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
EXAMPLE : 
Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input("Enter the number of steps:"))
    insertion_list = []
    print("The number of steps are going to be: " + str(N))
    for i in range(0,N):
        step=input("Enter the step along with parameters if applicable:")
        step = step.split(" ")
        if step[0] == 'insert':
           insertion_list.insert(int(step[1]), int(step[2]))
        elif step[0] == 'print':
            print(insertion_list)
        elif step[0] == 'remove':
            for i in insertion_list:
                print(i)
                if i == int(step[1]):
                    insertion_list.remove(i)
        elif step[0] == 'append':
            insertion_list.append(int(step[1]))
        elif step[0] == 'sort':
            insertion_list.sort()
        elif step[0] == 'pop':
            insertion_list.pop()
        else:
            insertion_list.reverse()


