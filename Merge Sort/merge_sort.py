def merge_sort(arr):
    # Если длина массива 0 или 1, он уже отсортирован
    if len(arr) > 1:
        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]

        # Рекурсивно сортируем левую и правую часть
        merge_sort(left_part)
        merge_sort(right_part)

        # Индексы для итерирования
        i = j = k = 0

        # Слияние отсортированных частей
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы левой части (если есть)
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        # Добавляем оставшиеся элементы правой части (если есть)
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

# Пример использования
numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers)
print(numbers)  # Результат: [3, 9, 10, 27, 38, 43, 82]



"""
В коде есть несколько ключевых моментов:

Рекурсия: если массив достаточно большой, разделяем его на две части, сортируем каждую.
Фаза слияния (while i < len(left_part) and j < len(right_part)): здесь мы сравниваем первые неиспользованные элементы из левой и правой части и помещаем меньший из них в итоговый массив.
Добавление «хвоста»: когда закончились элементы в одной из частей, нужно просто добавить остаток другой части.
"""