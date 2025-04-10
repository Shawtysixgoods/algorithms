def shell_sort(arr):
    n = len(arr)     # n - размер списка
    gap = n // 2     # Начальный шаг (промежуток). Берем половину длины списка.

    # 1. Главный Цикл Уменьшения Шага
    while gap > 0:
        # Этот цикл будет повторяться, пока шаг не станет 0.
        # С каждым разом gap будет уменьшаться.

        # 2. Цикл "Сортировки Вставками с Шагом gap"
        # Аналогичен внешнему циклу в сортировке вставками, но...
        for i in range(gap, n):
            # ...начинается не с 1, а с gap!
            # i - это индекс элемента, который мы сейчас пытаемся "вставить"
            # в его подсписок с шагом gap.

            # 3. Запоминаем Вставляемый Элемент
            temp = arr[i]
            # Сохраняем значение arr[i] (наш "key" из сортировки вставками).

            # 4. Готовимся Сдвигать Назад с Шагом gap
            j = i
            # j - это текущая позиция, куда мы ПОКА ЧТО можем вставить temp.
            # Начнем с исходной позиции i.

            # 5. Цикл Поиска Места и Сдвига с Шагом gap
            # Аналогичен внутреннему while в сортировке вставками, но...
            while j >= gap and arr[j - gap] > temp:
                # ...проверяем два условия:
                # j >= gap: Убеждаемся, что позиция j-gap (куда мы смотрим назад) существует в списке.
                # arr[j - gap] > temp: Проверяем, больше ли элемент на расстоянии gap СЛЕВА, чем наш temp.
                # Если оба условия верны, значит arr[j-gap] нужно сдвинуть вправо.

                # 6. Сдвиг Элемента Вправо (на gap позиций)
                arr[j] = arr[j - gap]
                # Элемент arr[j-gap] копируется на место arr[j].

                # 7. Двигаемся Дальше Назад с Шагом gap
                j -= gap
                # Уменьшаем j на величину шага, чтобы сравнить temp
                # со следующим элементом слева в этом же "подсписке с шагом".
                # Возвращаемся к проверке `while`.

            # 8. Вставка Элемента на Освободившееся Место
            # Цикл while закончился. Либо j стало меньше gap, либо arr[j-gap] оказалось <= temp.
            # Значит, правильное место для temp - это текущая позиция j.
            arr[j] = temp

        # 9. Уменьшение Шага для Следующего Прохода
        gap //= 2
        # Делим шаг на 2 (целочисленно). В следующий раз будем сортировать
        # элементы, стоящие ближе друг к другу.
        # Возвращаемся к началу `while gap > 0`.

# Пример:
numbers = [12, 34, 54, 2, 3]
shell_sort(numbers) # Запускаем
print(numbers)      # Получаем: [2, 3, 12, 34, 54]