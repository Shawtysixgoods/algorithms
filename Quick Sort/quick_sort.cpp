#include <iostream>
#include <vector>
using namespace std;

// Рекурсивная функция быстрой сортировки.
// Принимает вектор чисел и возвращает новый отсортированный вектор.
vector<int> QuickSort(const vector<int>& List) {
    // Базовый случай: если размер массива <= 1, сортировать не нужно
    if (List.size() <= 1) {
        return List;
    }

    // Опорный (pivot) элемент — последний элемент массива
    int pivot = List.back();

    // Два массива для значений меньше/больше опорного
    vector<int> leftList;
    vector<int> rightList;

    // Разделяем элементы относительно pivot
    for (size_t i = 0; i < List.size() - 1; i++) {
        if (List[i] < pivot) {
            leftList.push_back(List[i]);    // отправляем в левую часть
        } else {
            rightList.push_back(List[i]);   // отправляем в правую часть
        }
    }

    // Рекурсивный вызов для подмассивов
    vector<int> sortedLeft = QuickSort(leftList);
    vector<int> sortedRight = QuickSort(rightList);

    // Склеиваем результат: отсортированные левые + pivot + отсортированные правые
    sortedLeft.push_back(pivot);
    sortedLeft.insert(sortedLeft.end(), sortedRight.begin(), sortedRight.end());

    return sortedLeft;
}

int main() {
    // Пример: массив чисел для сортировки
    vector<int> data = {10, 7, 8, 9, 1, 5};

    // Сортировка массива
    vector<int> sorted = QuickSort(data);

    // Вывод результата
    cout << "Отсортированный массив: ";
    for (int x : sorted) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
