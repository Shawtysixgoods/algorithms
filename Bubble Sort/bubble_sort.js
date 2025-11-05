function bubbleSort(arr) {
  const n = arr.length;
  
  for (let i = 0; i < n; i++) {
    let swapped = false;
    
    // На каждой итерации самый большой элемент "всплывает" в конец
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Обмен элементов
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }
    
    // Если обмена не было, массив уже отсортирован
    if (!swapped) break;
  }
  
  return arr;
}

// Пример использования
console.log(bubbleSort([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]
