fn bubble_sort(arr: Array[Int]) -> Array[Int] {
  let new_arr = arr.copy()
  for i in 0..<new_arr.length(){
    for j in 1..<(new_arr.length() - i){
      if(new_arr[j - 1] > new_arr[j]){
        new_arr.swap(j - 1, j)
      }
    }
  }
  return new_arr
}
