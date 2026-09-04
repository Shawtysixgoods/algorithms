# pip install perfplot matplotlib

import perfplot
import random


def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def quick_sort_builtin(arr):
    return sorted(arr)


bench = perfplot.bench(
    setup=lambda n: [random.randint(0, 1000) for _ in range(n)], # как генерировать данные масштаба N
    kernels=[
        bubble_sort,
        quick_sort_builtin
    ],
    labels=["Bubble Sort", "Built-in Sort"],
    n_range=[2**k for k in range(2, 10)], # размеры массивов: от 4 до 512 элементов
    xlabel="Размер массива (N)",
    title="Сравнение алгоритмов сортировки"
)

bench.print()
bench.show()
