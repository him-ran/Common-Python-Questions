'''
This is for conversion of a decimal number into its binary format and viceversa.
'''
original_num = int(input("Enter the decimal number: "))
num = original_num
binary_list = []
binary_num = ""
bin_dec_converted = 0
while num >= 1:
    remainder = num%2
    binary_list.append(remainder)
    num = int(num/2)
binary_list.append(1)
for i in range(len(binary_list)-1,-1,-1):
    binary_num = binary_num + str(binary_list[i])
print("The binary converted value of " + str(original_num) + " is: " + binary_num)