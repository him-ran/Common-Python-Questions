# integersums
""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""


def getsum(num):
    try:
        sums = 0
        for i in range(0, num + 1): sums = sums + i
        return sums
    except:
        raise Exception("There is some issue.")


if __name__ == "__main__":
    number = int(input("Enter the number: "))
    sumOfRange = getsum(number)
    print("The sum is : " + str(sumOfRange))
