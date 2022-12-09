def insertionsort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    i: int = 1
    while (i < len(sorting)):
        j: int = i
        while (sorting[j] < sorting[j-1] and j > 0):
            sorting[j-1] , sorting[j] = sorting[j] , sorting[j-1]
            j -= 1
        i += 1
    return sorting

def bubblesort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    i: int = 0
    alreadysort: int = 0
    while (i <= alreadysort):
        j = 0
        while (j < len(sorting)-(i+1)):
            if sorting[j] > sorting[j+1]:
                sorting[j] , sorting[j+1] = sorting[j+1] , sorting[j]
            else:
                alreadysort += 1
            j += 1
        i += 1
    return sorting

def selectionsort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    i: int = 0
    while (i < len(sorting)):
        least_index: int = i # the index where the least number is located
        j: int = i
        while (j < len(sorting)):
            if (sorting[least_index] > sorting[j]):
                least_index = j
            j += 1
        if (least_index != i):
            sorting[i] ,sorting[least_index] = sorting[least_index], sorting[i]
        i += 1
    return sorting

def quicksort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    if (len(sorting) < 2): return sorting
    else:
        left: list[int | float] = []
        right: list[int | float] = []
        pivot = sorting.pop(len(sorting)-1)
        i: int = 0
        while (i < len(sorting)):
            if (sorting[i] < pivot): left.append(sorting[i])
            else: right.append(sorting[i])
            i += 1
        return quicksort(left) + [pivot] + quicksort(right)
    
def mergesort(List: list[int | float]) -> list[int | float]:
    sorting: list[int | float] = List.copy()
    # [a,b,c]
    if (len(List) < 2):
        return sorting
    else:
        mid: int = len(sorting)//2
        return __merging(mergesort(sorting[0:mid]),mergesort(sorting[mid:len(sorting)]))
    
def __merging(List1: list[int | float],List2: list[int | float]) -> list[int | float]:
    if (not (len(List1) and len(List2))):
        return List1 + List2
    else:
        ListC: list[int | float] = []
        Intermediate: int | float
        while (len(List1) + len(List2)):
            if (len(List1) and len(List2)):
                if (min(List1) < min(List2)): Intermediate = List1.pop(__index_min(List1))
                else: Intermediate = List2.pop(__index_min(List2))
            else:
                if (not len(List1)): Intermediate = List2.pop(__index_min(List2))
                else: Intermediate = List1.pop(__index_min(List1))
            ListC.append(Intermediate)
        return ListC

def __index_min(List: list[int | float]) -> int:
    mini: int = 0
    i: int = 0
    while (i < len(List)):
        if (List[mini] > List[i]):
            mini = i
        i += 1
    return mini