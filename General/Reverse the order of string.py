'''
This is the program to reverse the naming order using Python code
'''
import  sys
#Method 1: Using the split function
print("METHOD 1 :")
string1="Himanshu Ranjan is cool"
print("Initial string: " + string1)
string1 = string1.split(" ")
tempValue = " "
string_length = len(string1)
for i in range(string_length-1, -1, -1):
    tempValue = tempValue+string1[i] + " "
print("Reversed String:" +tempValue)

#Method2: Without the split function
index = 0
def split(text, index_value):
    temp_var = ""
    global index
    length = (len(text))
    for i in range(index_value, length, 1):
        if i <= length:
            if text[i] != " ":
                index = index + 1
                temp_var = temp_var + text[i]
                if i == length-1:
                    empty_list.append(temp_var)
            else:
                index = index + 1
                empty_list.append(temp_var)
                split(text, index)
                return

print("METHOD 2 :")
name2 = "Himanshu Ranjan is cool"
print("Initial string: " + name2)
empty_list = []
index = 0
split(name2, index)
tempValue2 = ""
empty_lis_len = len(empty_list)
for i in range(empty_lis_len-1, -1, -1):
     tempValue2 = tempValue2 + empty_list[i] + " "
print("Reversed String: " +tempValue2)

#Method3:Without split function and without the append function
print("METHOD 3 :")
name3 = "Himanshu Ranjan is cool"
print("Initial string: " + name3)
intermediate_string = ""
temp_var2 = ""
for i in range(len(name3)-1, -1, -1):
    if name3[i] != " ":
        temp_var2 = name3[i] + temp_var2
        if i == 0:
            intermediate_string = intermediate_string + temp_var2 + " "
    else:
        intermediate_string = intermediate_string + temp_var2 + " "
        temp_var2 = ""
print("Reversed String: " +intermediate_string)
