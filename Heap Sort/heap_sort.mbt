/// Преобразует поддерево с корнем `start_index` в Max-Heap (пирамиду).
fn heapify(arr: Array[Int], n: Int, start_index: Int) -> Unit {
  let mut i = start_index
  
  while true {
    let mut largest = i
    let left = 2 * i + 1
    let right = 2 * i + 2
    // Если левый дочерний элемент больше корня
    if left < n && arr[left] > arr[largest] {
      largest = left
    }
    // Если правый дочерний элемент больше текущего наибольшего
    if right < n && arr[right] > arr[largest] {
      largest = right
    }
    // Если наибольший элемент не корень, меняем их местами
    // и продолжаем просеивание вниз
    if largest != i {
      arr.swap(i, largest)
      i = largest // Переходим к следующему уровню (вместо рекурсивного вызова)
    } else {
      // Иначе свойство кучи выполнено, прерываем цикл
      break
    }
  }
}
/// Пирамидальная сортировка (Heap Sort).
pub fn heap_sort(arr: Array[Int]) -> Array[Int] {
  let new_arr = arr.copy()
  let n = new_arr.length()

  if n <= 1 {
    return new_arr
  }

  // 1. Построение Max-Heap
  // Начинаем с последнего узла, у которого есть потомки, и идем к корню (индекс 0)
  // Идиоматичный цикл for в MoonBit
  for i = n / 2 - 1; i >= 0; i = i - 1 {
    heapify(new_arr, n, i)
  }

  // 2. Извлечение элементов из кучи
  // Меняем местами корень (самый большой элемент) с последним элементом
  for i = n - 1; i > 0; i = i - 1 {
    new_arr.swap(i, 0)
    // Восстанавливаем свойство кучи для оставшейся неотсортированной части
    heapify(new_arr, i, 0)
  }

  return new_arr
}

// Тестовый блок, использующий встроенную систему тестирования MoonBit
test "heap_sort_basic" {
  // 1. Обычный несортированный массив
  let arr1 = [5, 3, 4, 1, 2]
  inspect(heap_sort(arr1), content="[1, 2, 3, 4, 5]")
  
  // 2. Уже отсортированный массив
  let arr2 = [1, 2, 3, 4, 5]
  inspect(heap_sort(arr2), content="[1, 2, 3, 4, 5]")
  
  // 3. Массив отсортированный в обратном порядке (худший случай)
  let arr3 = [9, 8, 7, 6]
  inspect(heap_sort(arr3), content="[6, 7, 8, 9]")
  
  // 4. Массив с повторяющимися элементами
  let arr4 = [4, 2, 2, 8, 3, 3, 1]
  inspect(heap_sort(arr4), content="[1, 2, 2, 3, 3, 4, 8]")
  
  // 5. Граничные случаи (пустой массив и массив из одного элемента)
  let empty_arr : Array[Int] = []
  inspect(heap_sort(empty_arr), content="[]")
  inspect(heap_sort([42]), content="[42]")
}
