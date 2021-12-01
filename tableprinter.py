#!/usr/bin python
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)
print(colWidths)

def findLongest(mylist):
    longest = mylist[0][0]

    for outerList in range(len(mylist)):
        for innerList in range(4):
            if len(mylist[outerList][innerList]) > len(longest):
                longest = mylist[outerList][innerList]
    return longest


def printtable(mylist, longest):
    for outerList in range(4):
        for innerList in range(3):
            #print(innerList, outerList)
            print(mylist[innerList][outerList].rjust(len(longest)), end=" ")

        print("\n")

l = findLongest(tableData)
printtable(tableData, l)

