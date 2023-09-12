def quick_sort(a, low, high):
    index = partition(a, low, high)
    if low < index-1:  
        quick_sort(a, low, index-1)
    if index < high :
        quick_sort(a, index, high)

def partition(a, low, high) :
    mid = int(low + (high-low)/2)
    pivot = a[mid] 	    
    while (low <= high) :
        while (a[low] < pivot) :
            low += 1
        while (a[high] > pivot):
            high -= 1	                
        if (low <= high) :
            swap(a, low, high)
            low += 1
            high -= 1
    return low

def swap(a, i, j) :
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp