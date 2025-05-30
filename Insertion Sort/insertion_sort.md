## Что такое сортировка вставками?

Сортировка вставками (Insertion Sort) – это метод упорядочивания элементов массива (или списка) путем последовательной обработки каждого элемента и «вставки» его в нужное место среди уже отсортированных элементов слева.

### Аналогия из жизни

Представьте, что у вас на руках колода игральных карт. Вы берете карты по одной из «неотсортированной» стопки и вставляете их в нужное место в уже отсортированной части руки, чтобы карты лежали по возрастанию. Точно так же в программировании сортировка вставками по очереди берет элементы массива и вставляет их туда, где они должны находиться.


### Суть Сортировки Вставками:
Считаем первый элемент уже отсортированным.
Берем следующий неотсортированный элемент (key).
Двигаемся назад по отсортированной части.
Сдвигаем вправо все элементы, которые больше key.
Вставляем key на освободившееся место.
Повторяем для всех неотсортированных элементов.
Этот метод хорошо работает для небольших списков или для списков, которые уже почти отсортированы. На больших и сильно перемешанных данных он будет медленнее, чем быстрая сортировка или сортировка слиянием.

### Визуальная блок-схема

```md
     ┌─────────────────────┐
     │ Начать сортировку   │
     └─────────────────────┘
                │
   ┌────────────▼──────────────────┐
   │ Переменная i идет с 1 до n-1  │
   └───────────────────────────────┘
                │
   ┌────────────▼───────────────────┐
   │ Текущий элемент (key) = arr[i] │
   │ j = i - 1                      │
   └────────────────────────────────┘
                │
   ┌────────────▼────────────────────────────────┐
   │ Пока j >= 0 и arr[j] > key:                 │
   │     сдвинуть arr[j] на arr[j+1]             │
   │     j = j - 1                               │
   └─────────────────────────────────────────────┘
                │
   ┌────────────▼────────────────────────────┐
   │ Когда закончилось сравнение,            │
   │ вставить key на позицию j+1             │
   └─────────────────────────────────────────┘
               │
     ┌─────────▼─────────┐
     │ Увеличить i на 1   │
     └────────────────────┘
               │
      ┌────────▼─────────┐
      │ Конец сортировки │
      └──────────────────┘

```

Здесь важно, что для каждого элемента мы «освобождаем» место, двигая вправо все, что больше текущего элемента.

### Когда стоит (и не стоит) использовать сортировку вставками?

#### Когда стоит:

Для небольших массивов, где размер данных невелик (например, менее тысячи элементов).
Когда массив частично отсортирован, и нужно его лишь «подправить». Сортировка вставками часто оказывается быстрой в ситуациях, когда большая часть элементов уже на своих местах.
Если важна простота кода и наглядность процесса вставки.

#### Когда не стоит:

При сортировке больших массивов, где требуется высокая производительность (лучше выбрать быструю сортировку, пирамидальную или сортировку слиянием).
Если диапазон данных широк, и нет особых преимуществ у механизма вставки (например, когда каждый элемент сильно отличается от других).