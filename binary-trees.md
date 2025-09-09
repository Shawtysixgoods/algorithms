# Полное руководство по бинарным деревьям

## Введение

Бинарные деревья являются одной из фундаментальных структур данных в информатике. Они представляют собой иерархические структуры данных, которые эффективно решают множество задач, включая поиск, сортировку и управление приоритетами.

## 1. Бинарные деревья: основы

### Определение

**Бинарное дерево** — это иерархическая структура данных, где каждый узел может иметь не более двух потомков, называемых левым и правым дочерними узлами.

### Основные компоненты

- **Узел (Node)** — элемент дерева, содержащий данные и указатели на дочерние узлы
- **Корень (Root)** — узел без родителя, вершина дерева
- **Лист (Leaf)** — узел без дочерних элементов
- **Родитель (Parent)** — узел, имеющий дочерние элементы
- **Ребро (Edge)** — связь между родителем и ребенком

### Терминология

- **Путь (Path)** — последовательность узлов от одного узла к другому
- **Глубина узла (Depth)** — длина пути от корня до узла
- **Высота дерева (Height)** — максимальная глубина среди всех листьев
- **Уровень (Level)** — узлы с одинаковой глубиной находятся на одном уровне

### Ключевые свойства бинарных деревьев

1. **Максимальное количество узлов на уровне i**: 2^i
2. **Максимальное количество узлов высоты h**: 2^(h+1) - 1
3. **Минимальное количество узлов высоты h**: h + 1
4. **Количество листьев**: узлы с двумя детьми + 1

### Типы бинарных деревьев

- **Полное бинарное дерево** — каждый узел имеет 0 или 2 ребенка
- **Совершенное бинарное дерево** — все внутренние узлы имеют 2 ребенка, все листья на одном уровне
- **Законченное бинарное дерево** — все уровни заполнены, кроме возможно последнего (заполняется слева направо)

### Обходы бинарного дерева

#### Прямой обход (Preorder): Корень → Левый → Правый

```
algorithm preorder(root):
    if root == null:
        return
    visit(root)
    preorder(root.left)
    preorder(root.right)
```

**Применение**: создание копии дерева, получение префиксных выражений

#### Симметричный обход (Inorder): Левый → Корень → Правый

```
algorithm inorder(root):
    if root == null:
        return
    inorder(root.left)
    visit(root)
    inorder(root.right)
```

**Применение**: получение элементов в отсортированном порядке (для BST)

#### Обратный обход (Postorder): Левый → Правый → Корень

```
algorithm postorder(root):
    if root == null:
        return
    postorder(root.left)
    postorder(root.right)
    visit(root)
```

**Применение**: удаление дерева, вычисление размера дерева, постфиксные выражения

## 2. Куча (Heap)

### Определение

**Куча** — это специализированное бинарное дерево, которое удовлетворяет свойству кучи и является законченным бинарным деревом.

### Свойство кучи

- **Max-Heap**: значение каждого узла больше или равно значениям его дочерних узлов
- **Min-Heap**: значение каждого узла меньше или равно значениям его дочерних узлов

### Представление кучи в массиве

Куча эффективно представляется массивом благодаря структуре законченного бинарного дерева:

- **Родитель узла i**: `(i-1)/2`
- **Левый ребенок узла i**: `2*i + 1`
- **Правый ребенок узла i**: `2*i + 2`

### Операции с кучей

#### Heapify (Просеивание)

Процесс восстановления свойства кучи:

```
algorithm heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        swap(arr[i], arr[largest])
        heapify(arr, n, largest)
```

#### Построение кучи

```
algorithm buildHeap(arr, n):
    for i from (n/2 - 1) down to 0:
        heapify(arr, n, i)
```

**Временная сложность**: O(n)

## 3. Max Heap (Макс-куча)

### Характеристики

- Корень содержит максимальный элемент
- Каждый родитель больше или равен своим детям
- Быстрый доступ к максимальному элементу

### Основные операции

#### Вставка (Insert)

```
algorithm insert(heap, value):
    heap.append(value)
    index = heap.size - 1
    
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] > heap[parent]:
            swap(heap[index], heap[parent])
            index = parent
        else:
            break
```

**Временная сложность**: O(log n)

#### Извлечение максимума (Extract Max)

```
algorithm extractMax(heap):
    if heap.isEmpty():
        return null
    
    max = heap[0]
    heap[0] = heap[heap.size - 1]
    heap.removeLastElement()
    heapify(heap, heap.size, 0)
    
    return max
```

**Временная сложность**: O(log n)

#### Получение максимума (Get Max)

```
algorithm getMax(heap):
    return heap[0]
```

**Временная сложность**: O(1)

## 4. Min Heap (Мин-куча)

### Характеристики

- Корень содержит минимальный элемент
- Каждый родитель меньше или равен своим детям
- Быстрый доступ к минимальному элементу

### Основные операции

#### Вставка (Insert)

```
algorithm insert(heap, value):
    heap.append(value)
    index = heap.size - 1
    
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] < heap[parent]:
            swap(heap[index], heap[parent])
            index = parent
        else:
            break
```

#### Извлечение минимума (Extract Min)

```
algorithm extractMin(heap):
    if heap.isEmpty():
        return null
    
    min = heap[0]
    heap[0] = heap[heap.size - 1]
    heap.removeLastElement()
    minHeapify(heap, heap.size, 0)
    
    return min
```

### Min Heapify

```
algorithm minHeapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        swap(arr[i], arr[smallest])
        minHeapify(arr, n, smallest)
```

## 5. Бинарное дерево поиска (BST)

### Определение

**Бинарное дерево поиска (BST)** — это бинарное дерево, где для каждого узла:
- Все узлы в левом поддереве имеют ключи меньше ключа узла
- Все узлы в правом поддереве имеют ключи больше ключа узла
- Оба поддерева также являются BST

### Свойства BST

1. **Упорядоченность**: симметричный обход дает элементы в отсортированном порядке
2. **Рекурсивная структура**: каждое поддерево является BST
3. **Эффективный поиск**: O(log n) в среднем случае

### Операции BST

#### Поиск (Search)

```
algorithm search(root, key):
    if root == null or root.key == key:
        return root
    
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
```

**Временная сложность**: O(h), где h — высота дерева

#### Вставка (Insert)

```
algorithm insert(root, key):
    if root == null:
        return createNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    else if key > root.key:
        root.right = insert(root.right, key)
    
    return root
```

#### Удаление (Delete)

```
algorithm delete(root, key):
    if root == null:
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
    else if key > root.key:
        root.right = delete(root.right, key)
    else:
        // Узел для удаления найден
        if root.left == null:
            return root.right
        else if root.right == null:
            return root.left
        
        // Узел с двумя детьми
        root.key = findMin(root.right)
        root.right = delete(root.right, root.key)
    
    return root
```

#### Поиск минимума/максимума

```
algorithm findMin(root):
    while root.left != null:
        root = root.left
    return root.key

algorithm findMax(root):
    while root.right != null:
        root = root.right
    return root.key
```

### Анализ сложности BST

- **Сбалансированное дерево**: O(log n) для поиска, вставки, удаления
- **Несбалансированное дерево**: O(n) в худшем случае (превращается в список)

## 6. Сравнение структур данных

### Бинарное дерево vs Массив vs Связный список

| Операция | Массив | Связный список | BST (сбалансированный) |
|----------|---------|---------------|----------------------|
| Доступ   | O(1)    | O(n)          | O(log n)            |
| Поиск    | O(n)    | O(n)          | O(log n)            |
| Вставка  | O(n)    | O(1)          | O(log n)            |
| Удаление | O(n)    | O(1)          | O(log n)            |

### Max Heap vs Min Heap

| Характеристика | Max Heap | Min Heap |
|---------------|----------|----------|
| Корень содержит | Максимум | Минимум |
| Извлечение приоритетного элемента | O(1) | O(1) |
| Вставка | O(log n) | O(log n) |
| Удаление | O(log n) | O(log n) |

## 7. Применения и алгоритмы

### Heap Sort (Пирамидальная сортировка)

```
algorithm heapSort(arr):
    n = arr.length
    
    // Построение кучи
    buildHeap(arr, n)
    
    // Извлечение элементов
    for i from n-1 down to 1:
        swap(arr[0], arr[i])
        heapify(arr, i, 0)
```

**Временная сложность**: O(n log n) во всех случаях
**Пространственная сложность**: O(1)

### Очередь с приоритетами

Кучи идеально подходят для реализации очередей с приоритетами:
- Вставка элемента: O(log n)
- Извлечение элемента с максимальным/минимальным приоритетом: O(log n)
- Просмотр элемента с максимальным/минимальным приоритетом: O(1)

### Самобалансирующиеся BST

#### AVL-деревья
- Строгое балансирование: высота поддеревьев различается не более чем на 1
- Гарантированная временная сложность: O(log n)
- Больше ротаций при вставке/удалении

#### Красно-черные деревья
- Менее строгое балансирование
- Каждый узел окрашен в красный или черный цвет
- Меньше ротаций при вставке/удалении
- Используются в стандартных библиотеках (map, set)

## 8. Практические примеры кода

### Реализация Max Heap на Python

```python
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        while i > 0:
            parent_i = self.parent(i)
            if self.heap[i] > self.heap[parent_i]:
                self.swap(i, parent_i)
                i = parent_i
            else:
                break
    
    def extract_max(self):
        if not self.heap:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
        
        return max_val
    
    def _heapify_down(self, i):
        while True:
            largest = i
            left = self.left_child(i)
            right = self.right_child(i)
            
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break
```

### Реализация BST на Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if node is None:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if node is None or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
```

## 9. Сложность и производительность

### Временные сложности

| Операция | Бинарное дерево | BST (сбалансированный) | BST (несбалансированный) | Heap |
|----------|----------------|----------------------|--------------------------|------|
| Поиск    | O(n)           | O(log n)             | O(n)                     | O(n) |
| Вставка  | O(1)           | O(log n)             | O(n)                     | O(log n) |
| Удаление | O(n)           | O(log n)             | O(n)                     | O(log n) |
| Минимум/Максимум | O(n)   | O(log n)             | O(n)                     | O(1) |

### Пространственные сложности

- **Представление указателями**: O(n) для хранения узлов
- **Массивное представление кучи**: O(n), но без дополнительных указателей
- **Рекурсивные алгоритмы**: O(h) для стека вызовов, где h — высота дерева

## 10. Выводы и рекомендации

### Когда использовать бинарные деревья

1. **BST**: когда нужен быстрый поиск и поддержание порядка элементов
2. **Max/Min Heap**: для очередей с приоритетами, алгоритмов сортировки
3. **Сбалансированные деревья**: для гарантированной производительности

### Преимущества

- Эффективные операции поиска, вставки и удаления
- Естественная иерархическая структура данных
- Возможность обхода в различном порядке
- Компактное представление в памяти (для куч)

### Недостатки

- Деградация производительности в несбалансированных BST
- Сложность реализации балансировки
- Дополнительная память для указателей (в представлении указателями)

Бинарные деревья являются фундаментальными структурами данных, понимание которых критично для эффективного программирования и решения алгоритмических задач.
