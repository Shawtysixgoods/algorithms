function shellSort(arr) {
  const n = arr.length;
  
  // Начинаем с большого gap и уменьшаем его
  for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
    
    // Выполняем сортировку вставкой для элементов на расстоянии gap
    for (let i = gap; i < n; i++) {
      const temp = arr[i];
      let j;
      
      // Сравниваем элементы, находящиеся на расстоянии gap
      for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
        arr[j] = arr[j - gap];
      }
      
      arr[j] = temp;
    }
  }
  
  return arr;
}

// Альтернативная последовательность gap (Knuth sequence: (3^k - 1) / 2)
function shellSortKnuth(arr) {
  const n = arr.length;
  
  // Вычисляем максимальный gap по последовательности Кнута
  let gap = 1;
  while (gap < n / 3) {
    gap = 3 * gap + 1;
  }
  
  while (gap > 0) {
    for (let i = gap; i < n; i++) {
      const temp = arr[i];
      let j;
      
      for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
        arr[j] = arr[j - gap];
      }
      
      arr[j] = temp;
    }
    
    gap = Math.floor(gap / 3);
  }
  
  return arr;
}

// Пример использования
console.log(shellSort([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]

console.log(shellSortKnuth([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]
