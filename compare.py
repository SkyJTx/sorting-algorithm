import random as r
import time as t
import sort
import sys


# realtime meaning net-elapsed time less than 50 ms
list1: list[int | float] = [r.randint(0,999) for i in range(1000)] # less than a sec (realtime sorting)
# list2: list[int | float] = [r.randint(0,999999) for i in range(1000000)] # less than 20 secs (general sorting)
# list3: list[int | float] = [r.randint(0,999999999) for i in range(1000000000)] # less than 3 hours (ultimate test)
# list4: list[int | float] = [r.randint(0,999999999999) for i in range(1000000000000)] # less than a day (for server)

print(f"Sorting Algorithms Time-Lapse (sort {len(list1)} random elements): ")

start, end = 0, 0
print("Bubble Sort : ",end="")
start = t.time()
sort.bubblesort(list1)
end = t.time()
print(f"{(end-start)*1000:.3f} ms")

start, end = 0, 0
print("Insertion Sort : ",end="")
start = t.time()
sort.insertionsort(list1)
end = t.time()
print(f"{(end-start)*1000:.3f} ms")

start, end = 0, 0
print("Quick Sort : ",end="")
start = t.time()
sort.quicksort(list1)
end = t.time()
print(f"{(end-start)*1000:.3f} ms")

start, end = 0, 0
print("Selection Sort : ",end="")
start = t.time()
sort.selectionsort(list1)
end = t.time()
print(f"{(end-start)*1000:.3f} ms")

start, end = 0, 0
print("Merge Sort : ",end="")
start = t.time()
sort.mergesort(list1)
end = t.time()
print(f"{(end-start)*1000:.3f} ms")

sys.modules[__name__].__dict__.clear()