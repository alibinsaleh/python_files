# Binary Search alogrithm

mylist = [10, 3, 45, 61, 99, 11, 23, 80, 72, 15, 1]
low = 0
high = len(mylist) -1
mid = (low + high)
print(mid)
def sort_list(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

    return l

sortedList = sort_list(mylist)

def binary_search(num, l):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end)
        guess = l[mid]
        if guess == num:
            return mid
        if guess > num:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(sortedList)
print(binary_search(77, sortedList))
print(binary_search(23, sortedList))


