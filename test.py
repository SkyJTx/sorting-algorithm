import random
from sort import *

element: int = 30
Test_List: list[int | float] = [random.randint(-element-1,element-1) for _ in range(element)]
print("Before Sort:",Test_List)
print()
print("Bubble Sort:",bubblesort(Test_List))
print("Insertion Sort:",insertionsort(Test_List))
print("Quick Sort:",quicksort(Test_List))
print("Selection Sort:",selectionsort(Test_List))
print("Merge Sort:",mergesort(Test_List))