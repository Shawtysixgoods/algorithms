
Измерение временной сложности и профилирование алгоритмов в Python

В этом руководстве собраны примеры использования ключевых библиотек и модулей для оценки производительности, временной сложности (Big-O) и профилирования кода в Python:
1. **`timeit`** — эталонный встроенный модуль для микро-бенчмаркинга.
2. **`big_o`** — автоматическое вычисление эмпирической асимптотической сложности $O(f(n))$.
3. **`timebudget`** — удобный декоратор и контекстный менеджер для замера блоков кода.
4. **`line_profiler`** — построчный профилировщик для поиска точных узких мест в функциях.

---

## 1. `timeit` (Встроенный модуль)

Стандартный инструмент Python для измерения точного времени выполнения небольших фрагментов кода. Он отключает сборщик мусора на время замеров и усредняет результаты по множеству запусков, минимизируя влияние фоновых процессов ОС.

### Установка
Установка не требуется (входит в стандартную библиотеку Python).

### Пример использования
```python
import timeit

# Тестовая функция
def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == "__main__":
    # Замер через timeit.timeit с передачей setup
    setup_code = "from __main__ import bubble_sort; import random; data = [random.randint(0, 1000) for _ in range(100)]"
    stmt_code = "bubble_sort(data)"

    runs = 100
    total_time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=runs)
    avg_time = total_time / runs

    print(f"[timeit] Среднее время на 100 элементов: {avg_time * 1000:.3f} мс (всего за {runs} запусков: {total_time:.4f} с)")

    # Вариант через timeit.repeat (рекомендуется: брать минимум из серии запусков)
    repeats = timeit.repeat(stmt=stmt_code, setup=setup_code, repeat=5, number=runs)
    best_time = min(repeats) / runs
    print(f"[timeit.repeat] Лучшее среднее время из 5 серий: {best_time * 1000:.3f} мс")

```

---

## 2. `big_o` (Оценка асимптотической сложности)

Библиотека запускает алгоритм на входных данных растущего размера $N$, замеряет время выполнения и методом наименьших квадратов подбирает наиболее подходящую кривую сложности: $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$, $O(n^3)$ или $O(2^n)$.

### Установка

```bash
pip install big-O

```

### Пример использования

```python
import big_o

# Тестируемые функции
def find_max(arr):
    """Линейный поиск O(N)"""
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m

def quadratic_pairs(arr):
    """Квадратичный алгоритм O(N^2)"""
    count = 0
    for x in arr:
        for y in arr:
            if x == y:
                count += 1
    return count

if __name__ == "__main__":
    # Генератор случайных целочисленных массивов длины n
    data_generator = lambda n: big_o.datagen.integers(n, 0, 10000)

    # 1. Измерение сложности для линейной функции
    best_fit_linear, fitted_linear = big_o.big_o(
        find_max,
        data_generator,
        min_n=100,
        max_n=10000,
        n_measures=10
    )
    print("--- Результат для find_max ---")
    print(f"Определенная сложность: {best_fit_linear}")

    # 2. Измерение сложности для квадратичной функции
    best_fit_quad, fitted_quad = big_o.big_o(
        quadratic_pairs,
        data_generator,
        min_n=50,
        max_n=1000,
        n_measures=8
    )
    print("\\n--- Результат для quadratic_pairs ---")
    print(f"Определенная сложность: {best_fit_quad}")

```

---

## 3. `timebudget` (Быстрый замер участков кода)

Легковесная библиотека для мониторинга времени выполнения блоков и функций. Работает как декоратор `@timebudget` или контекстный менеджер `with timebudget('name'):`, автоматически форматирует отчеты и агрегирует метрики.

### Установка

```bash
pip install timebudget

```

### Пример использования

```python
from timebudget import timebudget
import time

# Использование в качестве декоратора
@timebudget
def fetch_or_process_data():
    time.sleep(0.05)
    return [i ** 2 for i in range(50000)]

def run_pipeline():
    # Использование в качестве контекстного менеджера
    with timebudget("Генерация тестовых данных"):
        data = [i for i in range(100_000)]

    with timebudget("Сортировка данных"):
        sorted_data = sorted(data, reverse=True)

    with timebudget("Вызов декорированной функции"):
        for _ in range(5):
            fetch_or_process_data()

if __name__ == "__main__":
    run_pipeline()

    # Печать сводного отчета по всем задействованным блокам
    print("\\n--- Итоговый отчет timebudget ---")
    timebudget.report()

```

---

## 4. `line_profiler` (Построчное профилирование)

Позволяет точно увидеть, сколько времени тратится на каждую отдельную строку исходного кода внутри функции, процент от общего времени и количество вызовов строки.

### Документация

https://kernprof.readthedocs.io/en/latest/#line-profiler-basic-usage

### Установка

```bash
pip install line_profiler

```

### Запуск программно из Python-кода

```python
from line_profiler import LineProfiler
import random

def process_numbers(n):
    # Строка 1: аллокация
    numbers = [random.randint(1, 100) for _ in range(n)]
    
    # Строка 2: фильтрация четных
    evens = [x for x in numbers if x % 2 == 0]
    
    # Строка 3: вычисление квадратов
    squares = []
    for num in evens:
        squares.append(num ** 2)
        
    return sum(squares)

if __name__ == "__main__":
    profiler = LineProfiler()
    profiler.add_function(process_numbers)

    # Оборачиваем вызов функции в профилировщик
    wrapper = profiler(process_numbers)
    result = wrapper(100_000)

    # Вывод подробной построчной статистики в консоль
    profiler.print_stats()

```


## Сводная сравнительная таблица

| Библиотека / Модуль | Основное назначение | Дополнительная установка | Точность / Накладные расходы |
| --- | --- | --- | --- |
| **`timeit`** | Замер микро-оптимизаций, базовых операций и функций | Встроена в Python | Высокая точность, отключает GC |
| **`big_o`** | Автоматический эмпирический расчет асимптотической сложности $O(f(n))$ | `pip install big-O` | Замеряет на серии входных размеров $N$ |
| **`timebudget`** | Быстрое профилирование этапов пайплайна и функций декоратором | `pip install timebudget` | Очень низкие накладные расходы |
| **`line_profiler`** | Построчный детальный аудит узких мест алгоритма | `pip install line_profiler` | Высокая детализация (C-расширение) |


