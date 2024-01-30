def mutate_string(string, position, character):
    convertedList = list(string)
    convertedList[position] = character
    convertedString = ''.join(convertedList)
    return convertedString
