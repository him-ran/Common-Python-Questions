
import re, sys
firstString="Hello@"
secondString="elhlo234@"

#If it contains a special character
def checkSpecialCharacter(string):
    reg = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(reg.search(string) != None):
        print(string +" contains special characters. ")
        #To reframe the string affter removal of the special characters.
        string = [character for character in string if character.isalnum()]
        string = "".join(string)
        return (string)
    else:
        return string

#Calling the function to remove the special characters of a string if its exists.
firstString = checkSpecialCharacter(firstString)
secondString = checkSpecialCharacter(secondString)

#If the length of the string is not same
if len(firstString) == len(secondString):
    print("Yes the string length is same")
else:
    print("No, the length of the strings are not same")
    #sys.exit()

#if the characters in the string is same
firstString = firstString.lower()
secondString = secondString.lower()

if sorted(firstString) == sorted(secondString):
    print("Yes")
else:
    print("No")
