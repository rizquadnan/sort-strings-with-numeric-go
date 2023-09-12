def selection_sort(arr) :
  n = len(arr)
  for i in range(0, n-1) :
    min = i
    for j in range (i+1, n):
        if arr[j] < arr[min]:
            min = j
    swap(arr, i, min)
  return arr		
 
def swap(arr, i, j) :
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
