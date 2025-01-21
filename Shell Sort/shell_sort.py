def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальный шаг

    while gap > 0:
        # Сортировка вставками, но с шагом gap
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Двигаем элементы, которые больше temp, вправо
            # с учётом текущего gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # Переход к меньшему шагу
        gap //= 2

# Пример использования
numbers = [12, 34, 54, 2, 3]
shell_sort(numbers)
print(numbers)  # Например: [2, 3, 12, 34, 54]
