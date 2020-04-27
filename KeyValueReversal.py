"""
This code is to make the values of one dictionary as the keys of another/new dictionary.
Example:
    Input Dictionary: files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
        "Files1.txt": 'Himansu',
        "file2.txt": 'Himansu'
    }
    Output Dictionary: {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py'], 'Himansu': ['Files1.txt', 'file2.txt']}
"""
def group_by_owners(files):
    ownerDict = {}
    #For creation of a dict using the owner's name
    for value in files.values():
        ownerDict[value]=[]
    #For taking the filename from the dict and then adding it to the newDict.
    for key,value in files.items():
        if value in ownerDict.keys():
            ownerDict[value].append(key)
    return (ownerDict)


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
        "Files1.txt": 'Himansu',
        "file2.txt": 'Himansu'
    }
    print(group_by_owners(files))
