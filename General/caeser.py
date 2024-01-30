""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""


def returncharatcter(char, nums):
    asciivalue = ord(char)
    asciivalue = asciivalue + nums
    if asciivalue > 122:
        difference = asciivalue - 122
        asciivalue = 97 + (difference - 1)
    return chr(asciivalue)


def getletters(textmessage, shiftnum):
    encryptedmessage = ""
    for char in textmessage:
        if ord(char) in range(97, 127):
            encryptedchar = returncharatcter(char, shiftnum)
        else:
            encryptedchar = char
        encryptedmessage = encryptedmessage + encryptedchar
    print("Encrypted Message : " + encryptedmessage)


if __name__ == "__main__":
    text = input("Enter the message: ")
    num = int(input("Enter the number for encryption: "))
    getletters(text, num)
