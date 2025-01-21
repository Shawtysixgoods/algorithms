def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        # Поиск минимального в подмассиве arr[i..n-1]
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами текущий элемент и найденный минимум
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers)  # Результат: [11, 12, 22, 25, 64]

# Здесь min_index – это позиция, на которой находится минимальный элемент среди всех, что ещё не отсортированы. 
# После нахождения мы меняем местами элемент arr[i] (начало неотсортированной области) и элемент arr[min_index].

