function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];
    let j = i - 1;
    
    // Сдвигаем элементы, которые больше текущего
    while (j >= 0 && arr[j] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    
    // Вставляем текущий элемент на правильное место
    arr[j + 1] = current;
  }
  
  return arr;
}

// Пример использования
console.log(insertionSort([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]
