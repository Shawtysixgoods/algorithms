def quick_sort(arr):
    # Базовый случай: массив из 0 или 1 элемента не требует сортировки
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент (pivot)
    pivot = arr[0]
    left = []
    right = []
    equal = []

    # Раскладываем элементы по трем спискам
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    # Рекурсивно сортируем левую и правую часть
    return quick_sort(left) + equal + quick_sort(right)

# Пример использования
numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Результат: [1, 5, 7, 8, 9, 10]

# Основная идея: мы делим массив на три части и затем вызываем quick_sort для левой и правой части по отдельности.