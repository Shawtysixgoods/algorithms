def heapify(arr, n, i):
    # Индекс текущего "корня"
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Проверяем, не больше ли левый потомок?
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, не больше ли правый потомок?
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если largest изменился, значит нужно поменять элементы местами
    # и вызвать heapify для обновленного узла
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Шаг 1: Построение max-heap
    # Начинаем с последнего узла, у которого есть дети (n//2 - 1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Шаг 2: Извлекаем элементы из кучи один за другим
    for i in range(n - 1, 0, -1):
        # Меняем самый большой (корень) с последним элементом
        arr[i], arr[0] = arr[0], arr[i]
        # Восстанавливаем кучу для уменьшенного массива
        heapify(arr, i, 0)

# Пример использования
numbers = [12, 11, 13, 5, 6, 7]
heap_sort(numbers)
print(numbers)  # Результат: [5, 6, 7, 11, 12, 13]


"""
В блоке for i in range(n // 2 - 1, -1, -1) мы преобразуем массив в max-heap. 
Затем, начиная с конца массива, меняем верхушку кучи (максимум) с текущим последним элементом и уменьшаем размер кучи на 1, 
чтобы «зафиксировать» максимальный элемент на его конечном месте.
"""
