'''
This is for the conversion of Binary number to its decimal value
'''
import sys
dec_num = (input("Enter the decimal number: "))
dec_length = len(dec_num)
sums = 0
for num in range(dec_length-1, -1, -1):
    try:
        bin_num = int(dec_num[(dec_length-1)-num])
        if bin_num not in [1,0]:
            raise Exception
        power = 2**num
        product = int(bin_num) * int(power)
        sums = sums + product
    except:
        print("The number is not binary number.")
        sys.exit()
print("The decimal equivalent is  : " + str(sums))

    
