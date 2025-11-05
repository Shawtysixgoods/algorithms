function quickSort(arr) {
  // Базовый случай
  if (arr.length <= 1) return arr;
  
  // Выбираем опорный элемент (median-of-three стратегия для улучшения производительности)
  const pivot = arr[Math.floor(arr.length / 2)];
  
  const left = [];
  const middle = [];
  const right = [];
  
  // Разделяем массив на три части
  for (let x of arr) {
    if (x < pivot) {
      left.push(x);
    } else if (x === pivot) {
      middle.push(x);
    } else {
      right.push(x);
    }
  }
  
  // Рекурсивно сортируем и объединяем
  return [...quickSort(left), ...middle, ...quickSort(right)];
}

// Альтернативная реализация (сортировка на месте)
function quickSortInPlace(arr, low = 0, high = arr.length - 1) {
  if (low < high) {
    const pi = partition(arr, low, high);
    
    quickSortInPlace(arr, low, pi - 1);
    quickSortInPlace(arr, pi + 1, high);
  }
  
  return arr;
}

function partition(arr, low, high) {
  const pivot = arr[high];
  let i = low - 1;
  
  for (let j = low; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

// Пример использования
console.log(quickSort([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]
