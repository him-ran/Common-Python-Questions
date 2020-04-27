"""
This code is to make every possible combination of the elements from two lists.
"""


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        mergedList = []
        for i in self.ingredients:
            tempList = []
            for j in self.toppings:
                tempList.append(i)
                tempList.append(j)
                mergedList.append(tempList)
                tempList=[]

        return (mergedList)


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate","kaju"], ["chocolate sauce","sauce","kaju2"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
