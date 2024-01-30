'''
Description: Given a pattern and a string s, find if s follows the same pattern.
Example: Input: pattern = "abab", s = 'dog cat dog cat'
         Output: true
Explaination : pattern = 'abab'; s = 'dog cat dog cat'; return True
'a' represents 'dog' and 'b' represents cat
LeetCode Question URL : https://leetcode.com/problems/word-pattern/
'''

inputString = "dog dog dog dog"
input_pattern = "abba"

inputStringArray = inputString.split(" ")
inputPatternArray = list(input_pattern.strip())
comp_dict={}
patternTrue=True

if(len(inputStringArray) == len(inputPatternArray)):
    arrayLenth = len(inputStringArray)
    for elem in range(0,arrayLenth):
        # Making the pattern char as the key of the map, and assignig value to it.
        # Incase the pattern char is not a key in the map, then we add it to the map
        if((inputPatternArray[elem] not in comp_dict.keys())):
            if (inputStringArray[elem] in comp_dict.values()):
                patternTrue = False
            else:
                comp_dict[inputPatternArray[elem]] = inputStringArray[elem]
        else:
            # Else, we are checking if the key already exists, then th evalue of the pattern char key shud be the same as what was initially assigned with
            # If not, then returning a False
            if(comp_dict[inputPatternArray[elem]] != inputStringArray[elem]):
                patternTrue =False


    print(comp_dict)
    print(patternTrue)

else:
    print("They are of different lengths.")
# print(inputStringArray)
# print(inputPatternArray)
