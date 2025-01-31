def bubbleSort(l):
    """
    Needs to be implemented
    """
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


print(bubbleSort([3, 2, 4, 5]))
