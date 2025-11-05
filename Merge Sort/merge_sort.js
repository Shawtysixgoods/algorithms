function mergeSort(arr) {
  // Базовый случай: массив из одного элемента уже отсортирован
  if (arr.length <= 1) return arr;
  
  // Делим массив пополам
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  
  // Рекурсивно сортируем обе половины
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  const result = [];
  let i = 0;
  let j = 0;
  
  // Сравниваем элементы из обеих половин и добавляем меньший
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }
  
  // Добавляем оставшиеся элементы
  result.push(...left.slice(i));
  result.push(...right.slice(j));
  
  return result;
}

// Пример использования
console.log(mergeSort([64, 34, 25, 12, 22, 11, 90]));
// Результат: [11, 12, 22, 25, 34, 64, 90]
