def insertionsort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    i = 1
    while i < len(sorting):
        j = i
        while sorting[j] < sorting[j-1] and j > 0:
            sorting[j-1] , sorting[j] = sorting[j] , sorting[j-1]
            j = j - 1
        i = i + 1
    return sorting

def bubblesort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    i = 0
    alreadysort = 0
    while i <= alreadysort:
        j = 0
        while j < len(sorting)-(i+1):
            if sorting[j] > sorting[j+1]:
                sorting[j] , sorting[j+1] = sorting[j+1] , sorting[j]
            else:
                alreadysort = alreadysort + 1
            j = j + 1
        i = i + 1
    return sorting

def quicksort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    if (len(sorting) < 2): return sorting
    else:
        left: list[int | float] = []
        right: list[int | float] = []
        pivot = sorting.pop(len(sorting)-1)
        i = 0
        while (i < len(sorting)):
            if (sorting[i] < pivot): left.append(sorting[i])
            else: right.append(sorting[i])
            i = i + 1
        return quicksort(left) + [pivot] + quicksort(right)
