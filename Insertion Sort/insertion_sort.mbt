/// Сортировка вставками (Insertion Sort).
/// Возвращает новый отсортированный массив, оставляя исходный без изменений.
fn insertion_sort(arr: Array[Int]) -> Array[Int] {
  // Копируем массив, чтобы функция была чистой (не мутировала входные данные)
  let new_arr = arr.copy()
  let len = new_arr.length()
  
  // Если массив пуст или состоит из одного элемента, он уже отсортирован
  if len <= 1 {
    return new_arr
  }

  // Начинаем со второго элемента (индекс 1), так как первый элемент (индекс 0) 
  // условно считается уже отсортированной частью.
  for i in 1..<len {
    let key = new_arr[i]
    let mut j = i - 1
    
    // Идем справа налево по отсортированной части.
    // Сдвигаем элементы, которые больше `key`, на одну позицию вправо.
    // В MoonBit круглые скобки для условий while/if не нужны.
    while j >= 0 && new_arr[j] > key {
      new_arr[j + 1] = new_arr[j]
      j = j - 1
    }
    
    // Вставляем сохраненный `key` на освободившееся правильное место
    new_arr[j + 1] = key
  }
  
  return new_arr
}

// Тестирование с помощью встроенной системы макросов inspect!
test "insertion_sort_basic" {
  // 1. Обычный несортированный массив
  let arr1 = [5, 3, 4, 1, 2]
  inspect(insertion_sort(arr1), content="[1, 2, 3, 4, 5]")
  
  // 2. Уже отсортированный массив (Проверка лучшего случая - O(N))
  let arr2 = [1, 2, 3, 4, 5]
  inspect(insertion_sort(arr2), content="[1, 2, 3, 4, 5]")
  
  // 3. Массив, отсортированный в обратном порядке (Худший случай - O(N^2))
  let arr3 = [9, 8, 7, 6]
  inspect(insertion_sort(arr3), content="[6, 7, 8, 9]")
  
  // 4. Массив с повторяющимися элементами
  let arr4 = [4, 2, 2, 8, 3, 3, 1]
  inspect(insertion_sort(arr4), content="[1, 2, 2, 3, 3, 4, 8]")
  
  // 5. Граничные случаи: пустой массив и массив из одного элемента
  let empty_arr : Array[Int] = []
  inspect(insertion_sort(empty_arr), content="[]")
  inspect(insertion_sort([42]), content="[42]")
}
