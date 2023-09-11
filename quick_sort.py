#Divide and conquer, Time worst O(n^2) average O(n*logn), Space O(logn), n is array length
def quick_sort(a, low, high):
    index = partition(a, low, high)
    if low < index-1:  
        quick_sort(a, low, index-1)
    if index < high :
        quick_sort(a, index, high)
#Partition, Time O(n), Space O(1)
def partition(a, low, high) :
    mid = int(low + (high-low)/2) #middle of the array
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
#Swap two elements by index, Time O(1), Space O(1)
def swap(a, i, j) :
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp