from timebudget import timebudget

@timebudget
def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

@timebudget
def quick_sort(arr):
    return sorted(arr)

# Прогон тестов
import random
data = [random.randint(0, 1000) for _ in range(2000)]
bubble_sort(data)
quick_sort(data)

# Печать красивой сводки
timebudget.report()
